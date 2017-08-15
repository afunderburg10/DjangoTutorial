from django.contrib import admin

# Register your models here.
from todo.models import ToDoStatus, ToDoItem

admin.site.register(ToDoStatus)
admin.site.register(ToDoItem)
