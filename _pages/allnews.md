---
title: "News"
layout: textlay
excerpt: "Beadz Lab at National University of Singapore."
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}
<p>{{ article.date }} <br> {{ article.headline | markdownify}}</p>
{% endfor %}
