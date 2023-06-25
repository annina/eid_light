# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Light(models.Model):
	name = models.CharField(max_length=100)
	ident = models.TextField(unique=True, max_length=20)
	public = models.BooleanField(default=False);
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
	
	def __unicode__(self):
		return self.description
        

class Friends(models.Model):
	name = models.CharField(max_length=255)
	on = models.BooleanField(default=False)
	
	ident = models.TextField(unique=True, max_length=20)
	light = models.ForeignKey(
	'Light',
	on_delete=models.CASCADE,
	)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.description


class User(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.description
	