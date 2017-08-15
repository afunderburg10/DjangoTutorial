from django.shortcuts import render


# Create your views here.
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

# TODO - Create View
# TODO - needs new html page
# TODO - Add button to Create View to Home page

