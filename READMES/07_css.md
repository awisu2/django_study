# 07_css

[はじめての Django アプリ作成、その 6 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial06/)

- static/pollsディレクトリを作成

## hands on

```bash
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
```
