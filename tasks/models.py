from datetime import datetime

from django.db import models

from share.models import ExModel


class Task(ExModel):
    choice_text: str = models.CharField(max_length=200)
    votes: int = models.IntegerField(default=0)
    name: str = models.CharField(max_length=200)
    pub_date: datetime = models.DateTimeField("date published")

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class Note(ExModel):
    # taskに紐付いている
    task: int = models.ForeignKey(Task, on_delete=models.CASCADE)
    note: str = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return f"{self.id}: {self.note}"
