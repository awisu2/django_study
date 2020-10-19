# django study

## 前提条件

- python3 以上
- vscode 推奨
- windows の場合
  - bash 系のターミナルを前提としています。(Git Bash で十分)
- bin/util で、各種コマンド入力の自動化をしています
  - 一度 `bin/util` を実行してみてください
  - 実行時にどんなコマンドが実行されているかはなるべく出力するようにしています

## 参考 links

- [はじめての Django アプリ作成、その 1 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial01/)

## 1. 初期設定

`bin/util setup`

- venv の作成
- Django や必要パッケージのインストール

## 2. project の作成

`bin/util create_project django_study`

- プロジェクトの作成
- 新しいプロジェクトは新規ディレクトリで作成される
- django_study の部分はプロジェクト名、好きな名前をどうぞ

### 特殊処理：本番プロジェクトではは不要

`mv django_study _tmp && mv -f _tmp/* ./ && rm -rf _tmp`

この勉強ではパスがずれると進めずらいので無理やり中身を移動

## 3. サーバ起動

`bin/util start`

http://127.0.0.1:8000/ にアクセスすると django のデフォルト画面が表示されます。

## 4. アプリケーションの作成

実際の機能を持ったコードを書く場所を作成します
※ ここまでで作成したのはプロジェクト(機能の枠組み)で中身が空のためこの作業が必要です。細かい話は[こちら](./docs/application.md)

link: [はじめての Django アプリ作成、その 1 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial01/#creating-the-polls-app)

`bin/util start_app tasks`

### コードの実装

詳細は、link を見てください

1. 表示内容の作成: task/views.py, task/urls.py を修正
   - views.py: 実際に表示したい内容
   - urls.py: どんな uri で呼び出せるかの設定
2. プロジェクトと連結: django_study/urls.py を修正
   - 同じ方法で、新しいタスクを増やしていけば、それぞれに連結できます

## 5. データベース

- Database: デフォルトでは sqlite3 が設定されています(とりあえず動かすだけなら、十分)
  - sqlite 以外が必要な場合はこちらのドキュメントをお読みください
    - [はじめての Django アプリ作成、その 2 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial02/#database-setup)

### ファイルを更新/追記

_tasks/models.py_

```py
from datetime import datetime

from django.db import models


class Task(models.Model):
    choice_text: str = models.CharField(max_length=200)
    votes: int = models.IntegerField(default=0)
    name: str = models.CharField(max_length=200)
    pub_date: datetime = models.DateTimeField("date published")


class Note(models.Model):
    # taskに紐付いている
    task: int = models.ForeignKey(Task, on_delete=models.CASCADE)
    note: str = models.TextField(blank=True, default="")
```

_django_study/settings.py_

```py
INSTALLED_APPS = [
    ...
    "tasks.apps.TasksConfig",
]
```

\*NOTE: django は python manage.py を基準に実行されますが、実行時の対象アプリを INSTALLED_APPS で指定しています。

### 確認とテーブル作成

現在の migration 状況を確認

```bash
# 現在のmigrationの状況を確認
bin/util manage showmigrations
# tasks application だけを確認
bin/util manage showmigrations tasks

# migrate用のファイルを作成
bin/util manage makemigrations tasks
# 作成されたmigrateファイルを確認
cat tasks/migrations/0001_initial.py

# migrateを実行
bin/util manage migrate tasks 0001

# migrateの結果を確認([x]になっています)
bin/util manage showmigrations tasks
```

## 6. 実際に画面(ブラウザ)で見る

### 管理画面で見る

デフォルトで用意されている管理画面では、表示、更新/追加、削除がかんたんにできます。

[admin.md](docs/admin.md)

### 自作 view で見る

#### 1. 必要ファイルの作成

tasks/views.py

```py
from django.http import HttpResponse
from django.template import loader

from .models import Task


def index(request):

    tasks = Task.objects.all()
    template = loader.get_template("tasks/index.html")

    context = {"message": "hello world !", "tasks": tasks}
    return HttpResponse(template.render(context, request))
```

tasks/templates/tasks/index.html

\*NOTE:なぜ tasks ディレクトリを２重にしているかは別項

```html
<!DOCTYPE html>
<html lang="jp">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>

  <body>
    {% if message %}
    <p>{{message}}</p>
    {% endif %} {% if tasks %}

    <ul>
      {% for task in tasks %}
      <li>{{task}}</li>
      {% endfor %}
    </ul>
    {% else %}
    <p>データの登録がありません</p>
    {% endif %}
  </body>
</html>
```
