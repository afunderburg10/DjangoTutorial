from django.shortcuts import render, redirect

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

# TODO - Delete View
# TODO - Add delete button to row in Home Page
# TODO - have home page give an alert for confirmation of delete

# TODO - Edit View
# TODO - needs new html page - similar or same page as create
# TODO - Add edit button to row in Home Page


def detail(request, pk):
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

    context = {
        'form': form,
        'title': 'New'
    }
    return render(request, 'todo/edit.html', context=context)


def edit(request, pk):
    context = {
        'title': 'Edit'
    }
    return render(request, 'todo/edit.html', context=context)

# TODO - Create View
# TODO - needs new html page
# TODO - Add button to Create View to Home page

