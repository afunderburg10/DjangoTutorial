from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'webapp/home.html')


def polls(request):
    return render(request, 'webapp/polls.html')


def polls_detail(request):
    return HttpResponse('<h1>Polls Detail Page</h1>')
    # return render(request, 'webapp/polls.html')


def polls_results(request):
    return HttpResponse('<h1>Polls Results Page</h1>')
    return render(request, 'webapp/polls.html')


def polls_vote(request):
    return HttpResponse('<h1>Polls Detail Page</h1>')
    return render(request, 'webapp/polls.html')
