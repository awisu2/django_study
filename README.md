# django study

- [01_install](READMES/01_install.md)
- [02_migrate](READMES/02_migrate.md)
- [03_admin](READMES/03_admin.md)

## install

- python3 以上
- vscode 推奨
- windows の場合
  - bash 系のターミナルを前提としています。(Git Bash で十分)
- bin/util で、各種コマンド入力の自動化をしています
  - 一度 `bin/util` を実行してみてください
  - 実行時にどんなコマンドが実行されているかはなるべく出力するようにしています

### 初期設定

`bni/util setup`

以下の処理を行います。

- venv の作成
- Django や必要パッケージのインストール

## links

- [はじめての Django アプリ作成、その 1 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial01/)

## tips

- pip update: `python -m pip install -U pip`
- venv for windows: `.venv\Scripts\activate.bat`
- mysql を利用する場合、version3 あたりから mysqlclient が推奨されるようになった。pymysql は非推奨になった。
  - windows だと、python3.7 までなら`pip instal`できるが、それ以上はエラー(2020-10-11 確認)
- version: `django-admin --version`
- controller という名前でなく view
  - [] view 一つ、model 一つのチュートリアルだったので、もっと機能を追加する場合、新しく app を追加なのか、それともファイルを増やす方法があるのか知りたい

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
# {% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
```

## for windows

なんか cmd 経由で実行するとホスト情報の引き渡しでエラーになるので自前実行のこと
または、別のスクリプト経由にすべし

```cmd
SET DATABASE_ENGINE=django.db.backends.mysql
SET DATABASE_HOST=192.168.99.100
SET DATABASE_PORT=3306
SET DATABASE_NAME=django_study
SET DATABASE_USER=admin
SET DATABASE_PASSWORD=2wsxdr%tgbhu8

python manage.py runserver
```
