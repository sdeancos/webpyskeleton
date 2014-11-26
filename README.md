webpyskeleton
=============

web.py skeleton (web.py + routing json + jinja2)

Features:

- Routing from json file.
- Subapps system.
- Jinja2 Support.
- Flash message.

Dependencies
------------
- Web.py: pip install web.py
- Jinja2: pip install jinja2

Main
----

You can config you database in app/config.py and routes in urls.json

Try: python main.py

Test: http://localhost:8000/example



Example controller
------------------
```python
from app.config import render_template
from app.config import Flash
class index:
    def GET(self):
        """
        Example Controller WebpySkeleton
        """
        Controller:
        Flash.set('notice', 'Flash message')
        return render_template('bundles/ExampleBundle/views/index.jinja2')
```


Example view
------------
```jinja
{% extends "app/templates/base.jinja2" %}

{% block title %}Example View WebPySkeleton{% endblock %}

{% block head %}
    <link href="{{ CSS }}/main.css" rel="stylesheet">
        <script src="{{ JS }}/main.js"></script>
{% endblock %}

{% block content %}

    {% set flash = flash() %}
    {% if flash.notice %}
       {{ flash.notice[0] }}
    {% endif %}
    <h2>Example View WebPySkeleton</h2>
{% endblock %}
```
