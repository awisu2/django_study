# sdudy03

[はじめての Django アプリ作成、その2 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial02/#introducing-the-django-admin)

- メニューの追加は、`{projects}/settings.py` の **INSTALLED_APPS** に追記してある必要あり

## hands up

```bash
python manage.py createsuperuser
## admin, pass

python manage.py runserver
# access to http://127.0.0.1:8000/admin/

# adminのメニューにアプリを追加する
# edit polls/admin.py
>>>
from .models import Question

admin.site.register(Question)
<<<
```
