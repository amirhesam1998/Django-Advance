{% extends "mail_templated/base.tpl" %}

{% block subject %}
Account activision
{% endblock %}

{% block html %}
{{token}}
{% endblock %}