# view

## def と class の両方で作成できる

def

- 非常にシンプルで細かく書く必要あり

```py
def any_view(request[, args...])
```

class

- def とあまり変わらないが、method の区分けを method でできたり少し便利

```py
from django.views import View

class ListView(View):
    def get(self, request):
```

## 汎用ビュー

class ビューの拡張で、list, get などを補完

### ListView

[Generic display views \| Django documentation \| Django](https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#listview)

最低限 model だけセットしておけば、template の表示まで行ってくれる

```py
class ListView(generic.ListView):
    # 対象model(最低限これだけでOK)
    model = Task
    # テンプレート名(default: `{model}_list.html`)
    template_name = "tasks/list.html"
    # テンプレートでのコンテキスト名(default: 'object_list' と `{model}_list`)
    # 変更するわけではなくて追加する
    context_object_name = "rows"
    # ページング: `paginate_by={num}`
    paginate_by = 100
    # get_querysetの結果データ無しでも正常フラグ(Falseでraise 404)
    allow_empty = False

    def get_queryset(self):
        return self.model.objects.all()

    # viewにわたすパラメータをカスタマイズ
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = context["object_list"]
        return context
```

### DetailView

[Generic display views \| Django documentation \| Django](https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#listview)

最低限 model だけセットしておけば、template の表示まで行ってくれる

- template のデフォルト名: `{model}_detail.html`
- url からのパラメータ渡しは pk である必要がある
  - ex: `path('task/<int:pk>', views.DetailView.as_view(), name="task_detail")`

```py
class ListView(generic.DetailView):
    model = Task
```
