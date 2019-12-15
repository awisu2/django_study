# 05_form

[はじめての Django アプリ作成、その 4 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial04/)

- csrfの導入: `{% csrf_token %}`
- リクエストを受け取る: `request.POST['id']`
  - 値は常に文字列
  - 値がない場合 **KeyError** を発生
- views内でのurl生成: `reverse('polls:results', args=(question.id,))`
- 
- 
- 
- 
