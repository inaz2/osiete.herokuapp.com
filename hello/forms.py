# -*- coding: utf-8 -*-

from django import forms

class TopicForm(forms.Form):
    name = forms.CharField(label=u'名前', max_length=256)
    text = forms.CharField(label=u'質問', max_length=1024)
