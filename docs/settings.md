# django tips

## INSTALLED_APPS は不要なものを削れるのか？

ユーザ認証処理を利用する場合、基本的に削ることはできない。
不要及び危険と考えるなら、"django.contrib.admin"を消せるくらい

デフォルトで設定されているのはこちら

```py
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
]
```

"django.contrib.auth" は、"django.contrib.contenttypes" を relation で持っておりこの 2 つは消すことができない。
認証後 session を保つのなら、"django.contrib.sessions" も必要だろう。
これらがエラー時に表示するメッセージは、"django.contrib.messages" に設定されており。
完全な cli 運用でない限り、"django.contrib.staticfiles"は必要になる。
