# admin

django による GUI で database の管理を行うことができます

[はじめての Django アプリ作成、その 2 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial02/#introducing-the-django-admin)

## install

- INSTALLED_APPS はデフォルト設定でほぼ全て必要
- migrate してあること
- admin ユーザでないとアクセスできない
  - `bin/util manage createsuperuser`
- http://127.0.0.1:8000/admin

### 特定の Model を admin で扱えるように登録する

**{app}/admin.py**

```py
from django.contrib import admin

from .models import Foo, Bar

admin.site.register(Foo)
admin.site.register(Bar)
```

## かんたん Tips

- Model の `__str__`の返却値が admin 画面での各レコードの表示
