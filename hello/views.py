# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .forms import TopicForm

# Create your views here.
def index(request):
    variables = {'title': 'OSIETE: インターネットに聞いてみよう'}
    return render(request, 'index.html', {'variables': variables})


def popular(request):
    variables = {'title': '人気の質問 - OSIETE'}
    return render(request, 'popular.html', {'variables': variables})


def latest(request):
    variables = {'title': '新しい質問 - OSIETE'}
    return render(request, 'latest.html', {'variables': variables})


def ask(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            id = 1
            return HttpResponseRedirect("/topic/%d" % id)
    else:
        form = TopicForm()

    variables = {'title': '質問してみる - OSIETE'}
    return render(request, 'ask.html', {'variables': variables, 'form': form})


def topic(request, id):
    variables = {'title': 'xxx教えて！'}
    return render(request, 'topic.html', {'variables': variables})


def answer(request, id):
    return HttpResponseRedirect("/topic/%d" % id)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

