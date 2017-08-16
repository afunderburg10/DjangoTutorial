from django.utils import timezone
from django.db import models


class ToDoStatus(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class ToDoItem(models.Model):
    sort_order = models.BigIntegerField(unique=True)
    status = models.ForeignKey(ToDoStatus)
    text = models.CharField(max_length=500)
    create_date = models.DateField('date created', null=True, default=timezone.now)
    due_date = models.DateField('date due', null=True, blank=True)

    def __str__(self):
        return self.text
