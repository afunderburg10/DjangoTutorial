from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.utils import timezone

from todo.forms import ToDoItemForm
from todo.models import ToDoItem


def home(request):
    todo_list = ToDoItem.objects.order_by('sort_order')
    context = {
        'todos': todo_list
    }
    return render(request, 'todo/home.html', context=context)


def delete(request, pk):
    todo_item = get_object_or_404(ToDoItem, pk=pk)
    todo_item.delete()
    return redirect('todo:home')
# TODO - Delete View
# TODO - Add delete button to row in Home Page
# TODO - have home page give an alert for confirmation of delete


def detail(request, pk):
    # TODO - wire up data from DB
    # TODO - make detail.html look decent with info
    context = {
        'title': pk,
        'text': 'DUMMY TEXT'
    }
    return render(request, 'todo/detail.html', context=context)


def new(request):
    if request.method == 'POST':
        # Form submission logic
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.user = request.user
            todo_item.create_date = timezone.now()
            todo_item.save()
            return redirect('todo:detail', pk=todo_item.pk)
    else:
        # New page visit
        form = ToDoItemForm()

    for field in form.fields:
        form.fields[field].widget.attrs['class'] = 'form-control'
    form.fields['due_date'].widget.input_type = 'date'
    context = {
        'form': form,
        'title': 'New'
    }
    return render(request, 'todo/edit.html', context=context)


def edit(request, pk):
    # TODO - needs new html page - similar or same page as create
    # TODO - Add edit button to row in Home Page
    context = {
        'title': 'Edit'
    }
    return render(request, 'todo/edit.html', context=context)
