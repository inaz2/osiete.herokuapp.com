# -*- coding: utf-8 -*-

from django import forms

class TopicForm(forms.Form):
    text = forms.CharField(label='質問', max_length=1024)
    profile = forms.CharField(label='プロフィール', max_length=256, required=False)

class AnswerForm(forms.Form):
    text = forms.CharField(label='答え', max_length=1024)
    profile = forms.CharField(label='プロフィール', max_length=256, required=False)
