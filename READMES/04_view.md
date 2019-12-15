# 04_view

[はじめての Django アプリ作成、その 3 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial03/)

- django.shortcuts が便利
  - テンプレートの読み込みとHttpResponseの返却を一括で行う: `render`
  - データを読み込むが存在しなかった場合404を返却する: `get_object_or_404`
- app内の urls.py のpathで命名することにより、template内で url の記述が簡略化される
  - `urls.py` に **app_name** を指定することにより、名前空間を指定することも可能

## hands up

```bash
# 1. add view
# edit polls/views.py
# edit polls/urls.py

# show http://localhost:8000/polls/34/
```
