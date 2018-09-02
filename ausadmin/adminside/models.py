# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class category(models.Model):
	no=models.AutoField(primary_key =True)
	catname=models.CharField(max_length= 30)

class item(models.Model):
	name=models.CharField(max_length=30)
	quantity=models.IntegerField(blank=True)
	image=models.ImageField(upload_to='adminside/static/itemimages',blank=True)
	price=models.IntegerField(blank=True)
	categorychosen=models.CharField(max_length=40,blank= True)
	no2=models.AutoField(primary_key =True)


class user(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=30)
	adhar=models.IntegerField()
	phone=models.IntegerField()
	emailid=models.TextField(max_length=30)

class suggestions(models.Model):
	text=models.CharField(max_length=100)

