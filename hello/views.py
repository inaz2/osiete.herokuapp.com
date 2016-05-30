# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
try:
    from django.utils import simplejson as json
except ImportError:
    import json

from .models import Topic, Answer, TopicForm, AnswerForm

# Create your views here.
def index(request):
    topic_popular = Topic.objects.order_by('-viewcount')[:8]
    topic_latest = Topic.objects.order_by('-created')[:8]
    variables = {'title': 'OSIETE: インターネットに聞いてみよう'}
    return render(request, 'index.html', {'variables': variables, 'topic_popular': topic_popular, 'topic_latest': topic_latest})


def popular(request):
    page_number = request.GET.get('page', 1)
    topic_popular = Topic.objects.order_by('-viewcount')
    p = Paginator(topic_popular, 20)
    current_page = p.page(page_number)
    variables = {'title': '人気の質問 - OSIETE'}
    return render(request, 'popular.html', {'variables': variables, 'current_page': current_page})


def latest(request):
    page_number = request.GET.get('page', 1)
    topic_popular = Topic.objects.order_by('-created')
    p = Paginator(topic_popular, 20)
    current_page = p.page(page_number)
    variables = {'title': '新しい質問 - OSIETE'}
    return render(request, 'latest.html', {'variables': variables, 'current_page': current_page})


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


@require_POST
def answer(request, id):
    answer = Answer.objects.get(id=id)

    if request.method == 'POST':
        if request.POST.get('increment'):
            answer.likecount += 1
            answer.save()

    ctx = {'likecount': answer.likecount}
    return HttpResponse(json.dumps(ctx), content_type='application/json')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

