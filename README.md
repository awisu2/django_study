# django study

## study01

- [はじめての Django アプリ作成、その 1 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial01/)
- [Djangoを最速でマスターする part1 \- Qiita](https://qiita.com/gragragrao/items/373057783ba8856124f3)
  - 古い？というか、shellを使い始めた時点でエラーメッセージ出始めたので公式で勉強することにした

```bash
# 1. create project
django-admin startproject django_study
cd django_study
tree

# 2. run
# option "ip:port"
python manage.py runserver 0:8000

# 3. create app
python manage.py startapp polls
# edit
# polls/vies.py
```
