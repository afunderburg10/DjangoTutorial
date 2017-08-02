from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


# Create your views here.
from webapp.models import Question


def polls(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'webapp/polls.html', context=context)


def polls_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'webapp/polls_detail.html', context=context)


def polls_results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    context = {
        'question': question,
        'choices': choices
    }
    return render(request, 'webapp/polls_results.html', context=context)


def polls_vote(request, question_id):
    return HttpResponse('<h1>Polls Vote Page</h1><h2>Question ID: {0}</h2>'.format(question_id))
    # return render(request, 'webapp/polls.html')
