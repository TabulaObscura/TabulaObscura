---
layout: page
title: bookshelf
permalink: /books/
nav: true
---

> What an astonishing thing a book is. It's a flat object made from a tree with flexible parts on which are imprinted lots of funny dark squiggles. But one glance at it and you're inside the mind of another person, maybe somebody dead for thousands of years. Across the millennia, an author is speaking clearly and silently inside your head, directly to you. Writing is perhaps the greatest of human inventions, binding together people who never knew each other, citizens of distant epochs. Books break the shackles of time. A book is proof that humans are capable of working magic.
>
> -- Carl Sagan, Cosmos, Part 11: The Persistence of Memory (1980)

## Books that I am reading, have read, or will read

{::nomarkdown}
{% assign genres = "non-fiction,fiction" | split: "," %}
{% for genre in genres %}
  {% assign genre_books = site.books | where: "genre", genre %}
  <h1 id="g-{{ genre }}">{{ genre | capitalize }}</h1>
  <ul>
  {% for item in genre_books %}
    <figure class="cover">
      <a class="cover-link" href="{{ item.url | relative_url }}">
        {% if item.cover %}
          <img alt="{{ item.title }} cover" src="{{ item.cover | relative_url }}" style="height:200px">
        {% elsif item.olid %}
          <img alt="{{ item.title }} cover" src="https://covers.openlibrary.org/b/olid/{{ item.olid }}-L.jpg?default=false" style="height:200px">
        {% elsif item.isbn %}
          <img alt="{{ item.title }} cover" src="https://covers.openlibrary.org/b/isbn/{{ item.isbn }}-L.jpg?default=false" style="height:200px">
        {% endif %}
        {% if item.status %}
          {% assign statuses = 'abandoned,finished,interested,paused,queued,reading,reread' | split: ',' %}
          {% assign status = item.status | downcase | strip %}
          {% if statuses contains status %}
            <figcaption class="{{ status }}">{{ status | upcase }}</figcaption>
          {% else %}
            <figcaption class="uncategorized">UNCATEGORIZED</figcaption>
          {% endif %}
        {% else %}
          <figcaption class="uncategorized">UNCATEGORIZED</figcaption>
        {% endif %}
      </a>
    </figure>
  {% endfor %}
  </ul>
{% endfor %}
{:/nomarkdown}
