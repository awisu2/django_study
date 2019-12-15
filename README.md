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
# polls/urls.py
# django_study/urls.py
```

## study02

[はじめての Django アプリ作成、その2 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial02/)

### 重要ポイント

- modelに __str__ を追加して出力を見やすくできる
- 従属テーブルの操作が可能: `{parrent_table_row}.{child_table}_set`

### ドキュメント参照事項

- migrate時のカラム名の規則
- migrate実行時の名前など

### tutorial

```bash
# 1. database setting
# mysite/settings.py
# [optional] change DATABASES.default(with install driver)

# 2. migrate
python manage.py migrate

# 3. create model
# edit polls/models.py
# edit mysite/settings.py
#   add "'polls.apps.PollsConfig'" to INSTALLED_APPS

# 4. create migration files and run
python manage.py makemigrations polls

# 5. show sql by migrate
python manage.py sqlmigrate polls 0001

# 6. migrate
python manage.py migrate

# 7. touch db on shell
python manage.py shell

# shell >>>>>
from polls.models import Choice, Question
from django.utils import timezone

Question.objects.all()

# add row and show
q = Question(question_text="What's new?", pub_date=timezone.now())
q.id
q.save()
q.id
q.question_text
q.pub_date
Question.objects.all()

# update
q.question_text = "What's up?"
q.save()

# select with filter
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
Question.objects.get(pk=1)

Question.objects.get(id=2)

q = Question.objects.get(pk=1)
q.was_published_recently()

# 従属するchoiseテーブルレコードの操作
q = Question.objects.get(pk=1)
q.choice_set.all()

q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)

q.choice_set.all()
q.choice_set.count()

c.question

# 親テーブルの条件に一致するレコードを取得
Choice.objects.filter(question__pub_date__year=current_year)

# 削除
c = q.choice_set.filter(choice_text__startswith='Just hacking')
q.choice_set.count()
c.delete()
q.choice_set.count()
# shell <<<<<

# 8. django admin
python manage.py createsuperuser
# admin, pass
python manage.py runserver
# access to http://127.0.0.1:8000/admin/
```

