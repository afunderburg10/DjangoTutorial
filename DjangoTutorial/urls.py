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
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^example_template', TemplateView.as_view(template_name='example_template.html'), name='example_template'),
    url(r'^lisa_splash', TemplateView.as_view(template_name='lisa_splash.html'), name='lisa_splash'),
    url(r'^todo/', include('todo.urls')),
    url(r'^polls/', include('webapp.urls')),
    url(r'^admin/', admin.site.urls),
]
