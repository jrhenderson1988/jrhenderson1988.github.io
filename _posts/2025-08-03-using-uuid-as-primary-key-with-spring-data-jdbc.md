---
title: Using UUID as primary key with Spring Data JDBC
summary: "Navigating the pitfalls of using UUID as the primary key in Spring Data JDBC with MySQL, particularly around automatic generation and serialisation"
---

If you're like me, and you find JPA/Hibernate to be bulky, complex and full of gotchas, and you want
to try a simpler, lighter weight approach, you might want to try using JDBC directly. If you're
using Spring (and Spring Boot) you might consider using Spring Data JDBC instead of Spring Data JPA.

For the most part, Spring Data JDBC is similar to its JPA counterpart but with way less
functionality. You can still create objects that map to database records, and you can still use
Spring Data provided repositories to give you a starting point for interacting with the database.

However, there are tradeoffs. With the simplicity of JDBC, there are some things that don't quite
work as you might expect, coming from JPA and I found working with `UUID`s to be one of them.

The problems I faced seem surprisingly under-documented. So this post attempts to fill that gap.

## Context

I'm using MySQL and want to use a `UUID` as my primary key.

> I'm aware that it's often discouraged to do this as using UUID comes with significant drawbacks,
> often related to storage size and ordering (due to the randomness). If you want to read more about
> this,
> [this article](https://planetscale.com/blog/the-problem-with-using-a-uuid-primary-key-in-mysql)
> and also [this one](https://vladmihalcea.com/uuid-database-primary-key/) are good starting points

This is my schema:

```sql
CREATE TABLE IF NOT EXISTS `users` (
    `id` char(36) not null primary key,
    `name` varchar(255)
);
```

This is my Java object that models a record of this table:

```java
@Table("users")
@Getter
@Setter
public class User {
  @Id
  @Column("id")
  private UUID id;

  @Column("name")
  private String name;
  
  public User(UUID id, String name) {
    this.id = id;
    this.name = name;
  }
}
```

And here's my repository:

```java
@Repository
public interface UserRepository extends CrudRepository<User, UUID> {
  // ...
}
```

## Problem 1: Inserting vs Updating with Spring Data JDBC

Let's say I want to create a new user. You might consider doing something like this:

```java
var user = new User(null, "Foo");
userRepository.save(user);
```

But since we don't have a default value for our primary key, we get an exception:

```
java.sql.SQLException: Field 'id' doesn't have a default value
```

Okay, let's generate a UUID and provide it:

```java
var user = new User(UUID.randomUUID(), "Foo");
userRepository.save(user);
```

This time we get a different exception:

```
org.springframework.dao.IncorrectUpdateSemanticsDataAccessException: Failed to update entity [com.example.User@6fe517fc]; Id [d1089c08-151c-441a-9278-9cff0bd043e6] not found in database
```

This is because the default strategy that Spring Data JDBC uses to determine whether it should
perform an insert vs an update is whether the `@Id` annotated field is `null` or `0` (in the case of
numeric values). Since we've given it a non-null value, it'll try to do an update statement.

To work around this, we either need to make sure that we provide `null` as the `id` value and get it
to generate an `id` before inserting into the DB, or we can choose from a number of different 
strategies that can be used to tell the framework whether our object is "new" (we should insert) or 
not (we should update).

We'll go with the former for now, that we just want to generate an `id` before inserting. So how do
we do that?

```java
@Component
public class UserIdGenerator implements BeforeConvertCallback<User> {
  @Override
  public User onBeforeConvert(User user) {
    if (user.getId() == null) {
      user.setId(UUID.randomUUID());
    }
    return user;
  }
}
```

We create a bean (`@Component`) that implements `BeforeConvertCallback<User>`. The framework will 
call our callback just before running the insert or update SQL statement.

Crucially, it's called after it's already decided to perform an insert (because the value of `id` is
currently `null`):

```java
var user = new User(null, "Foo");
userRepository.save(user);
```

Our callback executes, then generates and sets a new `UUID` as the `id` field.

Now this _should_ do the trick, right? Nope!

```
java.sql.SQLException: Incorrect string value: '\xAC\xED\x00\x05sr...' for column 'id' at row 1
```

## Problem 2: Serialising UUID values with Spring Data JDBC

Spring Data JDBC doesn't natively support translating `UUID` values into a value that can be written
to MySQL. There are multiple different ways to store it in MySQL (such as `CHAR(36)` and 
`VARBINARY(16)`). When it comes to attempting to write this value to the database, it ends up 
falling back to attempting to write this in a sort of "catch-all" binary format, and since we're 
using `CHAR(36)`, we get an exception.

So how do we let Spring Data JDBC know how we want to serialise `UUID`?

There's a few ways to do this, but the one I landed on was to register some custom converters to 
handle reading and writing `UUID` types.

First, register a bean to handle converting `UUID` into `String`. Note that we're using 
`@WritingConverter` here so that the conversion is only applied when attempting to write `UUID` 
values to the database.

```java
@Component
@WritingConverter
public class UUIDToStringConverter implements Converter<UUID, String> {
  @Override
  public String convert(UUID source) {
    return source.toString();
  }
}
```

Next, we register a bean to handle converting `String` back to `UUID`. Note that we're using a
`@ReadingConverter` so that it only applies when turning a string-like value from MySQL (like
`CHAR(36)`) back into a `UUID`:

```java
@Component
@ReadingConverter
public class StringToUUIDConverter implements Converter<String, UUID> {
  @Override
  public UUID convert(String source) {
    return UUID.fromString(source);
  }
}
```

Finally, we need to register these custom converters with the framework by providing a 
`JdbcCustomConversions` bean that will be picked up by the framework to make our two new converters
available:

```java
@Configuration
public class JdbcConfiguration {
  @Bean
  public JdbcCustomConversions jdbcCustomConversions(
      UUIDToStringConverter uuidToStringConverter, StringToUUIDConverter stringToUUIDConverter) {
    return new JdbcCustomConversions(List.of(uuidToStringConverter, stringToUUIDConverter));
  }
}
```

Now we've both registered our `UUID` to `String` converters and we're also auto-generating a `UUID`
when the `id` field is `null` at the point of saving.

Does this work?

```java
var user = new User(null, "Foo");
var saved = userRepository.save(user);
System.out.println(saved.getId() + " / " + saved.getName());
// Outputs: 539c13bd-87e3-4730-9943-23360e1f8735 / Foo bar
```

Hurray!

## Bonus: Controlling whether you want to insert or update

I mentioned earlier that I chose to lean into the default insert vs update decision strategy, and
just use `null` as my default value for my primary key to indicate a new object, and I would 
automatically generate the `UUID` just before the query is executed.

But what if you want to pass in a `UUID` yourself, and you want control over whether to insert or
update?

### Persistable

There are [multiple strategies](https://docs.spring.io/spring-data/relational/reference/repositories/core-concepts.html#is-new-state-detection)
that Spring Data JDBC will apply to determine if your object represents a _new_ value. As previously
discussed, the default is to inspect the `@Id` annotated field to see if it's `null` or `0`.

There are other approaches such as implementing `Persistable` on your object so that you can 
customise the logic for determining if your object is new (should be inserted on `save`) or already
exists (should be updated on `save`).

```java
@Table("users")
@Getter
@Setter
public class User implements Persistable<UUID> {
  @Id
  @Column("id")
  private UUID id;

  @Column("name")
  private String name;
  
  @Transient
  private boolean isNew = false;

  public User(UUID id, String name) {
    this.id = id;
    this.name = name;
  }
}
```

Implementing  `boolean isNew()` from `Persistable<T>` on the class allows us to tell the framework 
that our value should be inserted (if true) or updated (if false).

The `@Transient` annotation tells the framework that the field is not intended to be saved to the
database.

You can of course implement it in whatever way you want. If you can somehow tell from just your 
object's internal state whether you want to insert without adding any additional fields, this 
approach would be great

In this (less than ideal) case, the `isNew` method is created by Lombok's `@Getter` and returns the
value of the `isNew` field meaning we have to manage additional internal state that's not really 
just the object's data. We can use the setter to mark the object to be inserted or updated:

```java
var user = new User(UUID.randomUUID(), "Foo");
user.setNew(true);
userRepository.save(user); // inserts a new user
```

This is not perfect as it means having to add another property, as well as setting it manually. We
could simplify this a bit by doing this in a `create` method in a service, but the field is still 
accessible from the outside.

### Explicit query on the repository

It's also possible to simply force a creation by adding a `@Query` to a method in our repository
interface. The downside here is that we need to specify all the fields individually:

```java
@Repository
public interface UserRepository extends CrudRepository<User, UUID> {
  @Modifying
  @Query("INSERT INTO users (id, name) VALUES (:id, :name)")
  void create(@Param("id") UUID id, @Param("name") String name);
}
```

We can't return a `User` here since we're not selecting any rows in this query. If we want to 
refresh the `User` object from the DB, we'd need to look it up again.

### JdbcAggregateTemplate

Another way, to force an insert or an update (and in my opinion, I think it's the best way) is to 
directly use `JdbcAggregateTemplate` to `insert` or `update` our entity, which guarantees insert or
update under the hood:

```java
var user = new User(UUID.randomUUID(), "Foo");
var savedNewUser = jdbcAggregateTemplate.insert(user);
var updatedUser = jdbcAggregateTemplate.update(savedNewUser);
```

We just pass our aggregate object to the method and the rest is taken care of.

If you've got a service class (e.g. `UserService`) that you're calling to create/update your 
entities (which we should be doing rather than using repositories directly), then this is a 
fantastic alternative.

## Conclusion

While Spring Data JDBC offers a simpler and more predictable alternative to JPA, it comes with its 
own quirks — especially when working with `UUID`s as primary keys. From understanding how 
insert/update detection works to customising UUID generation and serialization, there are several 
details to get right in order to avoid cryptic errors. Some of those details aren't particularly 
well documented.

If you're aiming for lightweight data access in Spring, it's well worth investing the time to
understand how Spring Data JDBC handles these edge cases.

On a final note, I do wish that we had direct `create` and `update` methods available on the 
`CrudRepository`, rather than just `save`. It would make things quite a bit easier and give more 
control to the developer. Similarly, I think it would be nice if there was a built-in way to handle
how `UUID`s are persisted, even if it means that the developer has to explicitly declare them.
