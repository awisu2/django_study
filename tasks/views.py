from django.http import HttpResponse
from django.template import loader

from .models import Task


def index(request):

    tasks = Task.objects.all()
    template = loader.get_template("tasks/index.html")

    context = {"message": "hello world !", "tasks": tasks}
    return HttpResponse(template.render(context, request))
