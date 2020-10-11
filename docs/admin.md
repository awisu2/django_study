# admin

django による GUI で database の管理を行うことができます

[はじめての Django アプリ作成、その 2 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial02/#introducing-the-django-admin)

## install

admin を利用する際は INSTALLED_APPS にデフォルトで設定されているものほぼすべてが必要です。(設定をいじらなければそのままで OK です)

その上で migrate されている必要があります

## 特定のアプリを admin で編集できるようにする

```py
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```
