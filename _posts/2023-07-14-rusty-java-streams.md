---
title: Rusty Java Streams
summary: ""
---

I've been tinkering with Rust for a few years at this point, on and off. Recently, I've been playing
around trying to understand how its iterators work. They feel fairly similar in nature to Java's 
streams. I thought it would be a fun exercise to try to partially re-implement Java's streams with
inspiration from Rust, including some common operations you typically see on streams, such as 
mapping, filtering and collecting results.

One important thing to note about both Rust's iterators and Java's streams is that they are both
_lazy_. What that means is that you can define all the operations that you want to occur upon the
stream up front, but nothing is applied until a terminal operation is executed. You can think of
this like a series of stages in a pipeline, where each stage operates on each item within the stream
individually, before passing it (unless it is discarded) onto the next. Each operation on the stream
can be considered a stage of the pipeline, but the it's the terminal operation that actually sends
the items in the stream through it and receives a result at the end.

Let's illustrate with some code:

```java
Stream<Integer> ints = Stream.of(1, 2, 3, 4).filter(n -> n > 2).map(n -> n * 2);
List<Integer> result = ints.collect(Collectors.toList());
```

In the first line of this example we've effectively set up our pipeline, with a `filter` stage first 
and a `map` stage second. Once the first line has been executed, no actions have been taken upon the
stream.

When the second line is executed, the `collect` method, which is a terminal operation, collects the
result of executing the stream into a list. Therefore, once the second line is executed, `result` 
will be a list containing two items: `[6, 8]`. The `map` operation was only ever called with values 
`3` and `4`. Values `1` and `2` were discarded by the `filter` stage and never made it to `map`.

Another thing to note about streams is that although they are typically used in Java to support 
functional programming, they typically contain state and once consumed, they can no longer be used:

```java
Stream<Integer> s = Stream.of(1, 2, 3, 4);
List<Integer> a = s.collect(Collectors.toList()); // returns list of [1, 2, 3, 4]
List<Integer> b = s.collect(Collectors.toList()); // throws IllegalStateException
```

It's a similar story with Rust's iterators. The `collect` method takes `self` (as opposed to `&self`
or `&mut self`) which typically means that calling `collect` _moves_ the iterator into the method
and a new value is returned. This has the effect of consuming the iterator.

## Getting started

Let's begin fleshing this out by defining some types. First, a `Stream`:

```java
public interface Stream<T> {
  <R> Option<R> next();
}
```

This interface is generic over `T`, which allows us to create streams of _any_ type. The only method
required to implement this interface is `next` which should return the next value in the stream. 
This is similar to how Rust's iterators work, where the `Iter` trait (analogous to a Java interface)
defines that implementations should provide a `next` method which returns the next value.

We've used another type parameter `R` here to represent the type of the next value, which might 
seem odd, but recall that you can have a stream which _maps_ to another stream of a different type. 
For instance, you might have a stream of `Person` and perhaps you want to turn that into a stream of
names which are strings, by calling the `getName` method on each `Person`.

Finally, there's a type `Option` that we've not yet defined:

```java
public class Option<T> {
  private final boolean some;
  private final T value;

  private Option(boolean some, T value) {
    this.some = some;
    this.value = value;
  }

  public boolean isSome() {
    return some;
  }

  public boolean isNone() {
    return !isSome();
  }

  public T getValue() {
    if (isNone()) {
      throw new IllegalStateException("Option is none");
    }
    return value;
  }

  public static <T> Option<T> some(T value) {
    return new Option<>(true, value);
  }

  public static <T> Option<T> none() {
    return new Option<>(false, null);
  }
}
```

This is a crude way of implementing Rust's `Option` type, which is _very_ similar to the `Optional`
type in Java land. It can either contain _some_ value, or be _none_. We use a boolean field `some`
which represents whether the type contains something and a field `value` of generic type `T` to hold
the actual value. There's a few methods there that we can use to tell if the `Option` is _some_ or
_none_ and a couple of static methods that we can use to construct either a `none` variant, or a 
`some` variant with a value.

We'll use this `Option` type to represent whether the `Stream::next` method has a _next_ value (it 
returns _some_ value), or if the stream has been consumed (it returns _none_).

## Terminal operations

The next piece of the puzzle is how we actually consume the stream and execute the pipeline we've 
set up.

In Java's streams, there's a method named `collect` which can be called on a stream with a 
_collector_ argument which dictates what type the resulting value will be and how it will be
generated from the stream.

Rust's iterators also have a `collect` method but instead of accepting an argument, it uses Rust's
powerful type system to work out which method will be called to build the result, by either passing 
a generic type parameter or by inferring the type from the type of the variable/binding receiving 
the result of the call.

Since we're doing this in Java, we'll go for a similar approach. First let's define the `Collector` 
type:

```java
public interface Collector<T, R> {
  R collect(Stream<T> stream);
}
```

The `Collector` is a single method interface over generic types `T` and `R` where `T` is the type of
the item in the stream upon which it operates and `R` is type that the collector returns. Each
`Collector` need only implement a `collect` method which accepts a `Stream<T>` and returns whatever
`R` is appropriate.

Next, in order to allow us to call `collect` on any stream, we'll add a default method to the 
`Stream` interface which accepts a `Collector` to allow it to consume the stream and return a value:

```java
public interface Stream<T> {
  // ...

  default <R> R collect(Collector<T, R> collector) {
    return collector.collect(this);
  }
}
```

The method added here defines a new generic type `R` and uses it to tie the return type of the 
`collect` method to the `R` type parameter of the collector. Given the `Collector` definition above,
this means that whatever type the `Collector` returns from its `collect` method will be the type 
that we return from `Stream`'s `collect` method. To illustrate this, take for example a 
`ListCollector` defined like this:

```java
public class ListCollector<T> implements Collector<T, List<T>> {
  // implementation omitted...
}
```

If we were to pass an instance of the above `ListCollector` into `Stream::collect`, then it would 
return a `List<T>` where `T` is the type of item the stream holds.

## Something concrete

That's enough of the initial setup for the time being. Let's start defining something more concrete.

We'll define a base implementation of the `Stream` that will just hold some data. Successive calls
to `next` will return each of the items within that stream, so we'll use an internal _"pointer"_
that will hold the index of the current item in `items`:

```java
public class ItemStream<T> implements Stream<T> {
  private final T[] items;
  private int pointer;

  public ItemStream(T[] items) {
    this.items = items;
    this.pointer = 0;
  }

  @Override
  @SuppressWarnings("unchecked")
  public <R> Option<R> next() {
    if (pointer >= items.length) {
      return Option.none();
    }
    T value = items[pointer++];
    return (Option<R>) Option.some(value);
  }
}
```

The `next` method does a simple bounds check, and returns `Option.none()` if the stream has been
consumed (we're out of bounds). If we're within bounds, we get the value that the internal pointer
is  currently looking at, and we increment the pointer for the next call. The returned value is
wrapped in an `Option.some(...)` to indicate to the caller that we're returning a valid value.

In this case, the type `T` of the stream is the same as the type of the returned value `R`, so we 
just cast to satisfy the compiler.

A quick example of how this works:

```java
Stream<String> s = new ItemStream<>(new String[] {"foo", "bar"});
s.next(); // Option.some("foo")
s.next(); // Option.some("bar")
s.next(); // Option.none()
s.next(); // Option.none()
```

The first calls to `next` return `Option.some(...)` values containing `"foo"` and `"bar"`
respectively, but all further calls to the stream will return `Option.none()`.

The `ItemStream` is the default concrete stream type, so let's make instantiating a stream a little
bit easier:

```java
public interface Stream<T> {
  // ...

  @SafeVarargs
  static <T> Stream<T> of(T... values) {
    return new ItemStream<>(values);
  }
}
```

If you're unfamiliar with _varargs_ syntax, this allows us to create a stream by calling 
`Stream.of(...)` and passing as many arguments of the same type as we want. It will return a 
`Stream<T>` where `T` is the type of the arguments we passed and `ItemStream` is the concrete
implementation of the stream. For instance: 

```java
Stream.of(1, 2, 3, 4); // Stream<Integer>
Stream.of("foo", "bar", "baz"); // Stream<String>
```

Finally, so that we're able to execute the stream and get something out of it, we'll create a 
concrete `Collector` implementation. Perhaps the `ListCollector` described previously would a good
starting point.

```java
public class ListCollector<T> implements Collector<T, List<T>> {
  @Override
  public List<T> collect(Stream<T> stream) {
    List<T> result = new ArrayList<>();
    while (true) {
      Option<T> next = stream.next();
      if (next.isNone()) {
        return result;
      }
      result.add(next.getValue());
    }
  }
}
```

Given a stream over type `T` we build a `List<T>` by first declaring an `ArrayList<T>` _result_ and 
continually pulling the _next_ item from the stream until the next item is _none_, at which point we
return the result. The value of every `Option.some(...)` variant pulled from the stream is added to
the list. Pretty simple.

> I did intend to avoid using the standard library entirely, but that would have meant creating my
own list type here, which is a little beyond the scope of the article, so I used the `List` 
interface and `ArrayList` implementation for the sake of brevity.

Given that Java's streams API provides a bunch of static methods that define commonly used 
collectors, we'll do the same here too:

```java
public final class Collectors {
  private Collectors() {}

  public static <T> ListCollector<T> toList() {
    return new ListCollector<>();
  }
}
```

Finally, we can actually do something with a stream, though it's not particularly useful:

```java
List<Integer> listOfInts = Stream.of(1, 2, 3, 4).collect(Collectors.toList());
assertEquals(List.of(1, 2, 3, 4), listOfInts);
```

## Stream operations

Right now, all we can do is define a new stream and collect it into a list. That doesn't provide
much value. Let's add some operations that make it more useful.

Before we do that, let's define another interface:

```java
public interface Function<T, R> {
  R apply(T value);
}
```

A single method interface over generic types `T` and `R` where `T` represents the type of an item 
(within a stream) and `R` represents a return type, which may be the same as `T` or completely 
different. The `apply` function accepts an argument of type `T` and returns a value of type `R`.

In Java 8 and above, lambdas can be used in place of single method interfaces like this one instead
of having to create a concrete or anonymous implementation.

The standard library has an interface almost identical to this one but it's trivial to write our
own.

### Map

First up, quite a common operation for those familiar with functional programming. The map operation
takes each value in the stream and transforms it into a new value by applying the provided function
to it. The new value need not be the same type:

```java
public class MappedStream<T, R> implements Stream<R> {
  private final Stream<T> stream;
  private final Function<T, R> fn;

  public MappedStream(Stream<T> stream, Function<T, R> fn) {
    this.stream = stream;
    this.fn = fn;
  }

  @Override
  @SuppressWarnings("unchecked")
  public <V> Option<V> next() {
    Option<T> next = stream.next();
    if (next.isNone()) {
      return Option.none();
    }
    return (Option<V>) Option.some(fn.apply(next.getValue()));
  }
}
```

The `MappedStream` implements our stream interface and therefore implements its `next` method to get
the next value. It accepts another stream that it will _wrap_ and a function that it can use to map
each value of the stream.

> Operations are just additional implementations of our stream class that _wrap_ another stream,
providing additional functionality in their `next` methods. Because they only actually do their work
when `next` is called, they are also lazy and will only ever actually do work when a terminal
operation (like calling `collect`) is invoked.

When the `next` method of the `MappedStream` is called, it asks for the `next` value of the inner 
stream that it wraps and calls its function with that value if it's an `Option.some(...)`. Otherwise
it just returns `Option.none()` without doing anything else if the inner stream returns
`Option.none()`.

To make calling `map` available to the stream, let's add a method to `Stream`:

```java
public interface Stream<T> {
  // ...

  default <R> Stream<R> map(Function<T, R> fn) {
    return new MappedStream<>(this, fn);
  }

  // ...
}
```

Calling `map` on a `Stream` returns a `MappedStream` which wraps the current stream object and
passes the function provided as an argument.

Now, let's use it:


```java
List<Integer> listOfInts = 
    Stream.of(1, 2, 3, 4).map(n -> n * 2).collect(Collectors.toList());
assertEquals(List.of(2, 4, 6, 8), listOfInts);
```

### Filter

Let's add another common stream operation. _Filter_ operates by passing each item of a stream to a
predicate and if that predicate holds _true_ then the item stays in the stream, otherwise it is
discarded:

```java
public class FilteredStream<T> implements Stream<T> {
  private final Stream<T> stream;
  private final Function<T, Boolean> predicate;

  public FilteredStream(Stream<T> stream, Function<T, Boolean> predicate) {
    this.stream = stream;
    this.predicate = predicate;
  }

  @Override
  @SuppressWarnings("unchecked")
  public <R> Option<R> next() {
    while (true) {
      Option<T> next = stream.next();
      if (next.isNone()) {
        return Option.none();
      } else if (predicate.apply(next.getValue())) {
        return (Option<R>) Option.some(next.getValue());
      }
    }
  }
}
```

This is reasonably similar in setup to the `MappedStream` above. However, instead of accepting a
function that maps an item of type `T` to another arbitrary type `R`, this time the function must
return a boolean value which represents whether the item belongs in the resulting stream.

The `next` method is implemented by continually reading from the wrapped stream and only returning
when either:
- the wrapped stream is exhausted i.e. the call to the wrapped stream's `next` method returns
  `Option.none()`, in which case `Option.none()` will be returned.
- or the wrapped stream's `next` method returns an `Option.some(...)` value which satisfies the
  predicate provided, in which case that value will be returned in an `Option.some(...)`.

This has the effect of throwing away values in the stream that don't satisfy the predicate,
resulting in fewer values that will ultimately be returned, assuming that at least one value is
discarded.

Let's add a `filter` method to `Stream` in order to create a `FilteredStream`:

```java
public interface Stream<T> {
  // ...

  default Stream<T> filter(Function<T, Boolean> fn) {
    return new FilteredStream<>(this, fn);
  }

  // ...
}
```

and let's see it in action:

```java
List<Integer> listOfInts =
    Stream.of(1, 2, 3, 4).filter(n -> n % 2 == 0).collect(Collectors.toList());
assertEquals(List.of(2, 4), listOfInts);
```

The predicate provided to `filter` in this example returns `true` if the item provided is an even
number, and false otherwise. This has the effect of throwing away the values `1` and `3` when
collecting the stream into a list.

### Combining operations

Let's use what we have so far to do something a bit more interesting:

```java
List<Integer> result = Stream.of("Java", "Rust", "Go", "Scala")
    .map(language -> language.toUpperCase())
    .filter(language -> language.contains("A"))
    .map(language -> language.length())
    .collect(Collectors.toList());
assertEquals(List.of(4, 5), result);
```

We start off with a stream of the names of 4 different programming languages.
- Calling `map`, we create a new `MappedStream<String, String>` wrapping our original stream and 
  passing in a `Function` that turns the given input string into uppercase.
- The next stage, `filter`, creates a new `FilteredStream<String>` that wraps the 
  `MappedStream<String, String>` from the previous step and passes a predicate that returns `true`
  if the string contains the substring `"A"`.
- Next, `map` creates a `MappedStream<String, Integer>` that wraps the `FilteredStream<String>` from
  the previous step and passes a function that returns the length of the given string.

Before calling `collect` we have a `Stream<Integer>` which concretely looks like this:

```java
Stream<Integer> stream = new MappedStream<String, Integer>(
    new FilteredStream<String>(
        new MappedStream<String, String>(
            new ItemStream<String>(
                new String[] {"java", "rust", "go", "scala"}),
            language -> language.toUpperCase()),
        language -> language.contains("A")),
    language -> language.length());
```

Before `collect` is called, nothing actually happens. But when we call `collect` and pass our
`ListCollector<Integer>`, the stream is consumed and a list containing `[4, 5]` is returned and the
assertion passes.

Adding some carefully placed `System.out.println(...)` statements, we can see the order in which the 
stream is consumed:

```
ListCollector:
  MappedStream:
    FilteredStream: 
      MappedStream:
        ItemStream:
         ∟ next -> java
       ∟ map(java) -> JAVA
     ∟ filter(JAVA) -> true
   ∟ map(JAVA) -> 4
# ListCollector result: [4]
  MappedStream:
    FilteredStream: 
      MappedStream:
        ItemStream:
         ∟ next -> rust
       ∟ map(rust) -> RUST
     ∟ filter(RUST) -> false
      MappedStream:
        ItemStream:
         ∟ next -> go
       ∟ map(go) -> GO
     ∟ filter(GO) -> false
      MappedStream:
        ItemStream:
         ∟ next -> scala
       ∟ map(scala) -> SCALA
     ∟ filter(SCALA) -> true
   ∟ map(SCALA) -> 5
# ListCollector result: [4, 5]
  MappedStream:
    FilteredStream: 
      MappedStream:
        ItemStream:
         ∟ next -> none
       ∟ none
       ∟ none
   ∟ none
ListCollector -> [4, 5]
```

Notice how each item in the stream is pushed through the entire pipeline, and how `"Rust"` and 
`"Go"` are filtered out early so they never reach the last `map` stage which returns the length of
the string.

## More Collectors

At this point, we've got most of the basics. We can create a stream, _map_ over each item, _filter_
out unwanted items and _collect_ items into a list. Let's finish off by building out some more
interesting collectors.

### Find

Given a stream of items, we want to be able to find the first item that holds true for a specified
predicate. If no such item exists, we can either provide a fallback item that is returned instead, 
or we can throw an exception.

```java
public class FindingCollector<T> implements Collector<T, T> {
  private final Function<T, Boolean> predicate;
  private final Option<T> fallback;

  public FindingCollector(Function<T, Boolean> predicate, T fallback) {
    this.predicate = predicate;
    this.fallback = Option.some(fallback);
  }

  public FindingCollector(Function<T, Boolean> predicate) {
    this.predicate = predicate;
    this.fallback = Option.none();
  }

  @Override
  public T collect(Stream<T> stream) {
    Option<T> current = stream.next();
    while (current.isSome()) {
      T value = current.getValue();
      if (predicate.apply(value)) {
        return value;
      }

      current = stream.next();
    }

    if (fallback.isNone()) {
      throw new IllegalStateException("Item not found");
    }

    return fallback.getValue();
  }
}
```

The `collect` method is reasonably simple. It just iterates through the items until it receives
`Option.none()`, applying the predicate against each item. If the predicate returns `true` for an
item, then we've found a match and the value is returned.

If we get to the end of the stream
(`Option.none()` has been returned), and no items have matched then we handle the case where no
matching item was found in the stream:
- If no fallback was specified (the single-argument constructor was used), then we throw an 
  `IllegalStateException`.
- If a fallback was specified, however (the two-argument constructor was used), then we can return 
  the fallback item.

> Note: this `find` collector works differently to the one we have in Java, which typically returns
`Optional.none()` if nothing is found and `Optional.of(value)` if there is a match.

Let's create a couple of static methods in `Collectors` for our convenience:

```java
public final class Collectors {

  // ...

  public static <T> FindingCollector<T> find(Function<T, Boolean> predicate) {
    return new FindingCollector<>(predicate);
  }

  public static <T> FindingCollector<T> find(Function<T, Boolean> predicate, T fallback) {
    return new FindingCollector<>(predicate, fallback);
  }
}
```

and let's use it:

```java
var result =
    Stream.of(8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
        .filter(n -> n % 2 == 0)
        .collect(Collectors.find(n -> n > 10));
assertEquals(12, result);
```
Here, we have a stream of integers from 8 to 20, and a `filter` function that only keeps _even_
numbers. Then we have a `find` collector with a predicate that returns true when the value given is
greater than 10.

When the `collect` method is called, the `FindingCollector`'s `collect` method is called with the
stream and starts pulling values out:
- `8` is received, put through the filter (8 is even) and then checked against the find predicate. 8
   is not greater than 10, so the collector moves onto the next value.
- `9` is received, put through the filter (9 is odd) and discarded. The find predicate is never
  called with 9.
- `10` is received, put through the filter (10 is even) and then checked against the find predicate.
10 is not greater than 10, so the collector moves onto the next value.
- `11` is received, put through the filter (11 is odd) and discarded. The find predicate is never
  called with 11.
- `12` is received, put through the filter (12 is even) and then checked against the find predicate.
  12 _is_ greater than 10, and so 12 is returned.

### Fold / Reduce

The `fold` (or `reduce`) operation _combines_ each item in a stream, using a given function to 
eventually build up a single return value. For example, imagine with have a stream of integers and
we want to sum them up; we could call a `fold` method on the stream and provide a function that adds
up every value and returns a single integer result.

The function we provide accepts two arguments, the accumulated value and the current value. The
current value is simply the item from the stream, retrieved from calling `Stream.next()`. The 
accumulated value is what we currently have after applying the function to all of the previous items
of the stream so far.

In our case, the `fold` operation also accepts an initial value, and that will be the accumulated
value for the very first item in the stream.

This may all seem a little, but hopefully the implementation and examples will help to illustrate.

We first need a way to provide function that accepts two arguments and returns a single value:

```java
public interface BiFunction<A, B, R> {
  R apply(A a, B b);
}
```

Just like `Function` that we declared earlier, this allows us to provide an anonymous function (or
lambda) in Java 8+. The difference here is that we've allowed for two arguments.

Onto the implementation of our `FoldingCollector`:

```java
public class FoldingCollector<T, R> implements Collector<T, R> {
  private final BiFunction<R, T, R> fn;
  private final R initialValue;

  public FoldingCollector(R initialValue, BiFunction<R, T, R> fn) {
    this.fn = fn;
    this.initialValue = initialValue;
  }

  @Override
  public R collect(Stream<T> stream) {
    R acc = initialValue;
    while (true) {
      Option<T> current = stream.next();
      if (current.isNone()) {
        break;
      }
      acc = fn.apply(acc, current.getValue());
    }
    return acc;
  }
}
```

The constructor accepts two arguments, a `BiFunction` which we'll use to pass our folding function,
and an initial value, which we'll use to start off the operation.

The `collect` method is of course the most interesting part. First, we take the `initialValue` and
assign it to `acc` (our accumulated value). For each `Option.some()` item in the stream, we apply
our `BiFunction`, passing the current `acc` as the first argument, and the current item of the
stream as the second. The result of applying our `BiFunction` is then assigned to `acc`, overwriting
the previous value. Once the stream has been consumed (`Stream.next()` returns `Option.none()`), we
break from the loop and return the current accumulated value.

Let's test it out:

```java
int result = Stream.of(1, 2, 3, 4).fold(1, (acc, curr) -> acc * curr);
assertEquals(24, result);
```

Starting off with a stream of numbers `1`, `2`, `3`, and `4`, we call `fold`, passing an initial
value of `1`, and a function that multiplies the accumulated value by the current value from the
stream. This has the effect of doing `1 * 1 * 2 * 3 * 4`, which happens to equal `24`. Let's step
through it:

- `acc` is set to the `initialValue`, which happens to be `1`
- The first iteration returns `Option.some(1)` and we call our function with `acc` (`1`) and the
  current value (`1`). We assign the result back to `acc` (1 * 1 = 1).
- The next iteration returns `Option.some(2)` and we call our function with `acc` (`1`) and the
  current value (`2`). We assign the result back to `acc` (1 * 2 = 2).
- The next iteration returns `Option.some(3)` and we call our function with `acc` (`2`) and the
  current value (`3`). We assign the result back to `acc` (2 * 3 = 6).
- The next iteration returns `Option.some(4)` and we call our function with `acc` (`6`) and the
  current value (`4`). We assign the result back to `acc` (6 * 4 = 24).
- The final iteration returns `Option.none()` and the loop breaks. The value held by `acc` (`24`) is
  then returned.

## Wrapping up

This exercise was no more than than an attempt to test out my rough mental model of how Java's
streams and Rust's iterators work. I wanted to build out a simplified implementation to illustrate
how I percieve things operating under the hood. In reality, the actual implementations of these 
features is undoubtedly more complex than shown here, with many more intricacies and use cases to
consider.

In doing this, I hoped to try to dispel some illusions and help others to achieve a better
understanding of what's happening behind the scenes when using Java streams and Rust iterators. I
hope this was useful to someone out there!