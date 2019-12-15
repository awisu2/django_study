# 06_test

[はじめての Django アプリ作成、その 5 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial05/)

- viewのテスト用に Clientモジュールが用意されている
- テスト内のレコード更新はロールバックされる

## hands up

### model test

```bash
# 1. cretat test
# edit polls/tests.py

# 2. run test
python manage.py test polls

# 3. modify code
# edit polls/models.py
python manage.py test polls
```

### view test

```bash
# 1. run shell
python manage.py shell
# shell >>>
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
client = Client()

response = client.get('/')
response.status_code

from django.urls import reverse
response = client.get(reverse('polls:index'))
response.status_code
response.content
response.context['latest_question_list']
# sehll <<<
```
