from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.ListView.as_view(), name="index"),
    path("", views.ListView.as_view(), name="task_list"),
    path("<int:pk>", views.DetailView.as_view(), name="task_detail"),
]
