# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render
# Create your views here.
from forms import SignupForm
from django.views.generic import TemplateView 
from forms import categoryform,itemform
from .models import category,item,user,suggestions

def signupform(request):
	
	return render(request, 'index.html');

@csrf_protect	
def addcat(request):
	form= categoryform(request.POST or None)
	if form.is_valid():
		form.save()
  
	context= {'form': form }
        
	return render(request, 'addcat.html', context)


def viewuser(request):
	
	data=user.objects.all()
	return render(request,'viewuser.html',{'data': data})

def viewcat(request):

	data=category.objects.all()
	
	return render(request, 'viewcat.html', {'data': data});

@csrf_protect	
def additem(request):
	d= itemform(request.POST, request.FILES)
	if d.is_valid():
		d.save()
	context= {'d': d }
	cats= category.objects.all()
	return render(request, 'additem.html',{'cats':cats});

def viewitem(request):
	data = item.objects.all()
	
	return render(request, 'viewitem.html',{'data':data});


def viewsuggs(request):
	
	data=suggestions.objects.all()
	return render(request,'viewsuggs.html', {'data':data});
	

def delfunction(request,part_id =None):
    if part_id!=None:
    	object = category.objects.get(no=part_id)
    	print part_id
    	object.delete()
    data=category.objects.all()
    return render(request,'viewcat.html',{'data':data})

def delitem(request,part_id =None):
    if part_id!=None:
    	object = item.objects.get(no2=part_id)
    	print part_id
    	object.delete()
    data=item.objects.all()
    return render(request,'viewitem.html',{'data':data})

def deluser(request,part_id =None):
    if part_id!=None:
    	object = user.objects.get(id=part_id)
    	object.delete()
    data=user.objects.all()
    return render(request,'viewuser.html',{'data':data})

