---
layout: page
menu_title: About
title: About me
permalink: /about
---
{% assign current_month = "now" | date: "%m" | abs %}
{% assign current_year = "now" | date: "%Y" | abs %}
{%- if current_month > 6 -%}
{% assign extra = 1 %}
{%- else -%}
{% assign extra = 0 %}
{%- endif -%}
{% assign pro = current_year | minus: site.professional_beginning_year | plus: extra %}
{% assign total = current_year | minus: site.beginning_year | plus: extra %}

I'm a software engineer and consultant, working as a Senior Developer at [Scott Logic](https://www.scottlogic.com/) based in Newcastle, UK.

I've been developing software professionally for about {{ pro }} years ({{ total }} years total) and if it's possible I think I love it more now than I did when I started. I'm full-stack but lean much more towards backend development and I find that my primary interests are within microservices, distributed systems, search engines and language design.

Over the course of my career I've used many languages and technologies, but I find that my passion lies within Kotlin, Java, Python and Go as well as Spring Boot and the JVM ecosystem as a whole. A lot of my free time is spent working on side projects, watching tech-talks and learning learn new languages and technologies; I currently find myself trying to pick up Rust and Scala.

I've had the chance to work on some interesting projects throughout my career. From travel agency websites and marketing intelligence applications to a car-sharing SaaS project and financial trading platforms.

When I'm not being a nerd, you can find me gaming, listening to music (Rock, Metal & ABBA), playing guitar and socialising. I love to travel and learn about other countries, cultures and languages; I particularly love Scandinavia. I lived in northern Sweden for a short period of time and speak Swedish more or less fluently. I'm also interested in aviation and my dream is to get my pilot's license.

<!--

I love:
- Kotlin / Java / Spring Boot
- Python / Django
- Go

I have significant experience with:
- PHP / Laravel
- JavaScript / TypeScript / Node.js / Express
- Web tech (HTML, CSS, SASS, LESS etc.)

Frameworks I've used:
- Laravel, Code Igniter, Yii
- Django
- Flask
- Spring (Boot, Cloud, MVC, WebFlux)
- Struts 2, Quarkus


<!--I'm passionate about Java, Kotlin and Python (and interested in Go) but very much a polyglot programmer, having used significantly more languages during my time. I live and breathe virtually anything to do with software development but find that my interests primarily lie within microservices, distributed systems, search engines and learning new languages.

I've used many frameworks such as Spring, Django, Laravel and Express as well as frontend technologies such as React, Angular and Vue. I consider myself to be a full-stack developer but I lean much more towards the backend.

I'm a polyglot, full-stack developer with a strong preference towards back end with ~{{ professional_experience }} years professional (~{{ total_experience }} years total) experience.

I'm passionate about Kotlin, Java, Python and Go but I also have considerable experience using PHP, JavaScript, TypeScript and Groovy as well as the standard web technologies (HTML, CSS, SASS). I additionally have some exposure to C#, as well as minor experience with Visual Basic and C/C++ from when I just started out. In the future, I'd like to learn more about Scala and Rust.

Over my career, I've had the opportunity to work with many different frameworks including Laravel, Code Igniter, Yii, Spring (Boot, Cloud, MVC, WebFlux etc.), Django, Flask, Node.js and Express. I've also experimented a lot with Micronaut, Quarkus, Struts 2 and .NET Core. On the front end, I've used React and jQuery extensively, but I've also used Vue, AngularJS.

<!-- I've done my share of... DevOps (CI/CD, Docker etc.), AWS

## Interests
## Experience

Throughout my career I've worked on some interesting projects, from travel agency websites and marketing intelligence applications to car-sharing services and trading platforms in the financial sector.

Much of my working life has been spent building Laravel applications with PHP and doing a considerable amount of frontend JavaScript. However, during my time with Scott Logic and in my own time I've found time to explore a variety of different technologies such as C# and .NET, Go, backend JavaScript with Node.js, TypeScript with a deep-dive into the AWS ecosystem.

## Personal life


<!--Throughout my career I've worked on everything from travel agency websites and marketing intelligence applications to car-sharing and financial trading platforms.

A considerable portion of my career has been spent developing PHP applications with Laravel

Much of my working life has been spent building Laravel applications with PHP and doing a considerable amount of frontend JavaScript. However, during my time with Scott Logic and in my own time I've found time to explore a variety of different technologies such as C# and .NET, Go, backend JavaScript with Node.js, TypeScript with a deep-dive into the AWS ecosystem.

I've used many frameworks such as Spring, Django, Laravel and Express as well as frontend technologies such as React, Angular and Vue. I consider myself to be a full-stack developer but I lean much more towards the backend.

-->
