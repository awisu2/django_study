# template

- url の補完: `{% url '{app_name}:{name}' [args...] %}`
  - app_name: urls.py の app_name フィールドで指定
  - name: urls.py で指定する path の name
- 引数: `{{ arg }}`
- function: `{% if arg %}exists{% endif %}`

## static

- assets 設置箇所
- `{app}/static`ディレクトリ配下

static をロードする

```html
{% load static %}
<!DOCTYPE html>
<html lang="jp">
  <head>
    ...
    <link
      rel="stylesheet"
      type="text/css"
      href="{% static 'tasks/style.css' %}"
    />
  </head>
</html>
```

## base タグを読み込む

extendsによって、機能を実装。

extendsは、読み込んだファイルを親として認識し、blockが一致するものを当てはめてtemplateを構成する。
親１、子１の構成が限界らしく、extendsファイルでextendsすると親ファイルのみになる

また、blockの中身は上書き形式

base.html

```html
{% load static %}
<!DOCTYPE html>
...
<body>
  {% block head %}
  <ul>
    <li><a href="{% url 'tasks:index' %}">top</a></li>
  </ul>
  {% endblock %}
  {% block content %}{% endblock %}
</body>

</html>
```

content.html

```html
{% extends "tasks/base.html" %}

{% block content %}
{% if message %}
<p>{{message}}</p>
{% endif %}

{% if object_list %}
<ul>
  {% for row in object_list %}
  <li><a href="{% url 'tasks:detail' row.id %}">{{row}}</a></li>
  {% endfor %}
</ul>
{% else %}
<p>データの登録がありません</p>
{% endif %}

{% endblock %}
```
