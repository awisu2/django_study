from django.http import HttpResponse, Http404
from django.template import loader
from django.views import View, generic

from .models import Task, Note


class ListView(generic.ListView):
    model = Task
    # テンプレート名(default: `{model}_list.html`)
    # template_name = "tasks/index.html"
    # テンプレートでのコンテキスト名(default: 'object_list')
    context_object_name = "rows"
    # ページング: `paginate_by={num}`
    paginate_by = 100
    # get_querysetの結果データ無しでも正常フラグ(Falseでraise 404)
    allow_empty = False

    def get_queryset(self):
        # INFO: 結果が0の場合404になる
        return self.model.objects.all()

    # get_query_setの結果を取得し
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = context["object_list"]
        return context


class DetailView(generic.DetailView):
    model = Task
