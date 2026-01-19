---
title: "Beadz Lab - Publications"
layout: gridlay
excerpt: "Beadz Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endfor %}
