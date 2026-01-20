---
title: "Beadz Lab - Team"
layout: gridlay
excerpt: "Beadz Lab: Team members"
sitemap: false
permalink: /team/
---

# People

 **We are  looking for new PhD students, Postdocs, and Master students to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**

## Staff
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  {% if member.website %}
  <h4><a href="{{ member.website }}" target="_blank">{{ member.name }}</a></h4>
  {% else %}
  <h4>{{ member.name }}</h4>
  {% endif %}
  <b>{{ member.role}} </b> <br> 
  <i>{{ member.info }} <br> </i> 
  
  {% if member.email %}
  email: <{{ member.email }}>
  {% endif %}
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  <li> {{ member.education3 | markdownify}} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  <li> {{ member.education3 | markdownify}} </li>
  <li> {{ member.education4 | markdownify}} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  <li> {{ member.education3 | markdownify}} </li>
  <li> {{ member.education4 | markdownify}} </li>
  <li> {{ member.education5 | markdownify}} </li>
  {% endif %}

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


# Alumni

## PhD
{% assign number_printed = 0 %}
{% for member in site.data.alumni_phd %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  {% if member.website %}
  <h4><a href="{{ member.website }}" target="_blank">{{ member.name }}</a></h4>
  {% else %}
  <h4>{{ member.name }}</h4>
  {% endif %}
  <i>{{ member.duration }} <br> {{ member.info }}</i>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


## Postdoc
{% assign number_printed = 0 %}
{% for member in site.data.alumni_postdoc %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  {% if member.website %}
  <h4><a href="{{ member.website }}" target="_blank">{{ member.name }}</a></h4>
  {% else %}
  <h4>{{ member.name }}</h4>
  {% endif %}
  <i>{{ member.duration }} <br> {{ member.info }}</i>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Master
{% assign number_printed = 0 %}
{% for member in site.data.alumni_master %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  {% if member.website %}
  <h4><a href="{{ member.website }}" target="_blank">{{ member.name }}</a></h4>
  {% else %}
  <h4>{{ member.name }}</h4>
  {% endif %}
  <i>{{ member.duration }} <br> {{ member.info }}</i>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Research Engineer
{% assign number_printed = 0 %}
{% for member in site.data.alumni_re %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  {% if member.website %}
  <h4><a href="{{ member.website }}" target="_blank">{{ member.name }}</a></h4>
  {% else %}
  <h4>{{ member.name }}</h4>
  {% endif %}
  <i>{{ member.duration }} <br> {{ member.info }}</i>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<div class="row">
<div class="col-sm-6 clearfix">
<h4>Exchange PhD Students</h4>
{% for member in site.data.alumni_exchange %}
{{ member.name }}
{% endfor %}
</div>
</div>

<figure>
<img src="{{ site.url }}{{ site.baseurl }}/images/group_photo.jpg" width="95%">
</figure>

