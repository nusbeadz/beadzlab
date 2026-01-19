---
title: "Beadz Lab - Pictures"
layout: piclay
excerpt: "Beadz Lab -- Pictures"
permalink: /gallery
---

# Gallery
(Left-click to see a larger image.)
{% assign number_printed = 0 %}
{% assign pics = site.static_files | where_exp: "f", "f.path contains '/images/gallery/'" | sort: "path" %}
{% for pic in pics %}

{% assign even_odd = number_printed | modulo: 4 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-3 clearfix">
<a href="{{ pic.path | prepend: site.baseurl }}" target="_blank" rel="noopener">
  <img src="{{ pic.path | prepend: site.baseurl }}" class="img-responsive" width="95%" style="float: left" />
</a>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd > 2 %}
</div>
{% endif %}


{% endfor %}

{% assign even_odd = number_printed | modulo: 4 %}
{% if even_odd == 1 %}
</div>
{% endif %}

{% if even_odd == 2 %}
</div>
{% endif %}

{% if even_odd == 3 %}
</div>
{% endif %}

<p> &nbsp; </p>
