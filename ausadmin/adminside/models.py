# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.
import uuid
class category(models.Model):
	no=models.AutoField(primary_key =True)
	catname=models.CharField(max_length= 30)

class item(models.Model):
	name=models.CharField(max_length=30)
	quantity=models.IntegerField(blank=True)
	image=models.ImageField(upload_to='adminside/static/itemimages',default= "adminside/static/images/play.png")
	price=models.IntegerField(blank=True)
	categorychosen=models.CharField(max_length=40,blank= True)
	no2=models.AutoField(primary_key =True)


class user(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=30)
	adhar=models.IntegerField()
	phone=models.IntegerField()
	emailid=models.TextField(max_length=30)
	password=models.CharField(max_length=30,default="pass")

class suggestions(models.Model):
	text=models.CharField(max_length=100)



class booking(models.Model):
	date=models.DateField(default=datetime.date.today)
	eventname=models.CharField(max_length=30)
	eventdate=models.CharField(max_length=30,default="NA")
	c1=models.CharField(max_length=30)
	c2=models.CharField(max_length=30)
	bookid=models.UUIDField(default=uuid.uuid4,editable=False,unique=True,max_length=10)
	user=models.CharField(max_length=30,default="user1")
	c3=models.CharField(max_length=30)
	c4=models.CharField(max_length=30)
	c5=models.CharField(max_length=30)
	c6=models.CharField(max_length=30)
	totalcost=models.CharField(max_length=30)