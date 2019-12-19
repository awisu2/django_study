# django study

- [01_install](READMES/01_install.md)
- [02_migrate](READMES/02_migrate.md)
- [03_admin](READMES/03_admin.md)

## links

- ことはじめ
  - [Djangoでの開発 ダイジェスト \- Qiita](https://qiita.com/zaburo/items/0e15f6c150caa13ca34c)
- 増殖するmodelsやviewsを分割する
  - [Djangoでモジュールを複数ファイルで構成する \- Qiita](https://qiita.com/RyoMa_0923/items/c4ca5bd070e823403fdf)

## tips

- pip update: `python -m pip install -U pip`
- venv for windows: `.venv\Scripts\activate.bat`
- mysqlを利用する場合、version3あたりからmysqlclientが推奨されるようになった。pymysqlは非推奨になり
- version: `django-admin --version`
- controllerという名前でなくview
  - [] view一つ、model一つのチュートリアルだったので、もっと機能を追加する場合、新しくappを追加なのか、それともファイルを増やす方法があるのか知りたい

## 簡易スタートまとめ

```bash
# create project -----
django-admin startproject django_study
cd django_study

# ★run
# option "ip:port"
python manage.py runserver 0:8000

# create app -----
python manage.py startapp polls
# edit
# polls/vies.py
# polls/urls.py
# django_study/urls.py


# database setting -----
# mysqlclient recommend by public. pyMySql can't use.
pip install mysqlclient

# mysite/settings.py
# [optional] change DATABASES.default(with install driver)

# migrate
python manage.py migrate

# create model
# edit polls/models.py
# edit mysite/settings.py
#   add "'polls.apps.PollsConfig'" to INSTALLED_APPS

# ★create migration files
python manage.py makemigrations polls

# show sql by migrate
python manage.py sqlmigrate polls 0001

# ★migrate
python manage.py migrate

# admin ----------
python manage.py createsuperuser
## admin, pass
# access to http://127.0.0.1:8000/admin/

# add view ----------
# edit polls/views.py
# edit polls/urls.py

# show http://localhost:8000/polls/34/

# test -----
# cretat test
# edit polls/tests.py

# run test
python manage.py test polls

# modify code
# edit polls/models.py
python manage.py test polls

# static css/image -----
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
```
