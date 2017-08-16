from django import forms

from .models import ToDoItem


class ToDoItemForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ('sort_order', 'status', 'text', 'due_date')
