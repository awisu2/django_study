# template

- url の補完: `{% url '{app_name}:{name}' [args...] %}`
  - app_name: urls.py の app_name フィールドで指定
  - name: urls.py で指定する path の name
- 引数: `{{ arg }}`
- function: `{% if arg %}exists{% endif %}`
