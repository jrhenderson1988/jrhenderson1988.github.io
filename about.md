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

Over the course of my career I've used many languages and technologies, but I find that my passion lies within Java, Kotlin, Go, Rust and Python. Much of my free time is spent working on side projects, watching tech-talks and learning learn new languages and technologies; I currently find myself trying to pick up Rust and Scala.

I've had the chance to work on some interesting projects throughout my career. From travel agency websites and marketing intelligence applications to a car-sharing SaaS project and financial trading platforms.

When I'm not being a nerd, you can find me gaming, listening to music (Rock, Metal & ABBA), playing guitar and socialising. I love to travel and learn about other countries, cultures and languages; I particularly love Scandinavia. I lived in northern Sweden for a short period of time and speak Swedish more or less fluently. I'm also interested in aviation and my dream is to get my pilot's license.
