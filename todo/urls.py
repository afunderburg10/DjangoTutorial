"""DjangoTutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

app_name = 'todo'
urlpatterns = [
    # ex: <site>/todo
    url(r'^$', TemplateView.as_view(template_name='todo/home.html'), name='home'),
    # # ex: <site>/polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.polls_detail, name='detail'),
    # # ex: <site>/polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.polls_results, name='results'),
    # # ex: <site>/polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.polls_vote, name='vote'),
]