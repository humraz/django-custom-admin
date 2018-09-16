# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render
# Create your views here.
from forms import SignupForm
from django.views.generic import TemplateView 
from forms import *
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



def register(request):
	form= loginform(request.POST or None)
	if form.is_valid():
		s=form.cleaned_data['name']
		p=form.cleaned_data['password']
		print s,p
		if user.objects.all().filter(name=s):
			user.objects.all().filter(name=s).update(password=p)
			return render(request,'register.html',{'f':"passed"})

		else:
			return render(request,'register.html',{'f':"failed"})
	return render(request,'register.html',{'f':""})

	



def afterlogin(request):
	s= request.session.get("username","NA")
	pas=request.session.get("password","NA")
	u=booking.objects.all().filter(user=s)
	return render(request,'logindex.html',{'user':s,'s':u})
def viewuserindex(request):
	
	
	return render(request,'userindex.html')

def viewuser(request):
	
	data=user.objects.all()
	return render(request,'viewuser.html',{'data': data})

def index(request):
	return render(request, 'index.html')

def feed(request):
	f=feedform(request.POST or None)
	if f.is_valid():
		f.save()
	return render(request,'feedback.html')




def login(request):
	f=loginform(request.POST or None)
	if f.is_valid():
		u=f.cleaned_data['name']
		p=f.cleaned_data['password']
		if u == "admin" :
			return render(request,'index.html')
		if user.objects.all().filter(name=u,password=p):
			request.session['username']=u
			request.session['password']=p

			s=booking.objects.all().filter(user=u)
			return render(request,'logindex.html',{'user':u,'s':s})
		
	return render(request,'loginn.html')


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
	data = category.objects.all()
	f=categoryform(request.POST or None)
	if f.is_valid():
		c=f.cleaned_data['catname']
		print c
		d= item.objects.all().filter(categorychosen=c)
		request.session['cc']=c
		return render(request, 'viewitem.html',{'data':d});

	return render(request, 'viewitem1.html',{'cats':data});

import re

def book(request):
	items= item.objects.all()
	cat=category.objects.all()
	f2=bookform2(request.POST or None)
	if f2.is_valid():
		evname=f2.cleaned_data['eventname']
		c1= f2.cleaned_data['c1']
		c2= f2.cleaned_data['c2']
		c3= f2.cleaned_data['c3']
		c4= f2.cleaned_data['c4']
		c5= f2.cleaned_data['c5']
		t=[]
		t=re.findall(r'\d+', c1+c2+c3+c4+c5)
		tot=0
		for i in t:
			tot=tot+int(i)
		print tot
		
		f2.save()

		booking.objects.all().filter(eventname=evname).update(totalcost=tot)

		return render(request,'booking.html',{'item':items, 'cats':cat,'s':"booked",'tot':tot})
	f=bookform(request.POST or None)
	print "hi"
	if f.is_valid():
		s= request.session.get("username","NA")
		print s
		name=f.cleaned_data['eventname']
		c1= f.cleaned_data['c1']
		c2= f.cleaned_data['c2']
		c3= f.cleaned_data['c3']
		c4= f.cleaned_data['c4']
		c5= f.cleaned_data['c5']
		s1= item.objects.all().filter(categorychosen=c1)
		s2= item.objects.all().filter(categorychosen=c2)
		s3= item.objects.all().filter(categorychosen=c3)
		s4= item.objects.all().filter(categorychosen=c4)
		s5= item.objects.all().filter(categorychosen=c5)
		return render(request,'booking.html',{'name':name,'usernn':s,'c1':c1,'c2':c2,'c3':c3,'c4':c4,'c5':c5,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s':'ok'})



	return render(request,'booking.html',{'item':items, 'cats':cat,'s':""})


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
    c=request.session['cc']
    data= item.objects.all().filter(categorychosen=c)
    return render(request,'viewitem.html',{'data':data})

def deluser(request,part_id =None):
    if part_id!=None:
    	object = user.objects.get(id=part_id)
    	object.delete()
    data=user.objects.all()
    return render(request,'viewuser.html',{'data':data})

