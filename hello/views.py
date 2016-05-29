# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Topic, Answer
from .forms import TopicForm, AnswerForm

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
            topic = Topic()
            topic.text = form.cleaned_data['text']
            topic.profile = form.cleaned_data['profile']
            topic.ipaddress = request.META.get('REMOTE_ADDR')
            topic.useragent = request.META.get('HTTP_USER_AGENT')
            topic.save()
            return HttpResponseRedirect("/topic/%d" % topic.id)
    else:
        form = TopicForm()

    variables = {'title': '質問してみる - OSIETE'}
    return render(request, 'ask.html', {'variables': variables, 'form': form})


def topic(request, id):
    topic = Topic.objects.get(id=id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = Answer()
            answer.topic = topic
            answer.text = form.cleaned_data['text']
            answer.profile = form.cleaned_data['profile']
            answer.ipaddress = request.META.get('REMOTE_ADDR')
            answer.useragent = request.META.get('HTTP_USER_AGENT')
            answer.save()
            return HttpResponseRedirect("/topic/%d" % topic.id)
    else:
        form = AnswerForm()

    topic.viewcount += 1
    topic.save()
    answers = topic.answer_set.order_by('created')
    variables = {'title': u"%s教えて！" % topic.text }
    return render(request, 'topic.html', {'variables': variables, 'topic': topic, 'answers': answers, 'form': form})


def answer(request, id):
    return HttpResponseRedirect("/topic/%d" % id)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

