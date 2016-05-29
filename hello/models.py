from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class Topic(models.Model):
    name = models.CharField(256)
    text = models.CharField(1024)
    ipaddress = models.GenericIPAddressField()
    useragent = models.CharField(1024)
    created = models.DateTimeField('date created', auto_now_add=True)
    viewcount = models.IntegerField()


class Answer(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(256)
    text = models.CharField(1024)
    ipaddress = models.GenericIPAddressField()
    useragent = models.CharField(1024)
    created = models.DateTimeField('date created', auto_now_add=True)
    likecount = models.IntegerField()
