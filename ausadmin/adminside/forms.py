from django import forms 
from .models import *
#creating our forms
class SignupForm(forms.Form):
	#django gives a number of predefined fields
	#CharField and EmailField are only two of them
	#go through the official docs for more field details
	name = forms.CharField(label='Enter your name', max_length=100)
	email = forms.EmailField(label='Enter your email', max_length=100)


from .models import category,item

class categoryform(forms.ModelForm):
    class Meta:
        model= category
        fields= ["catname",]


class itemform(forms.ModelForm):
    class Meta:
        model= item
        fields= ["name","quantity","image","price","categorychosen",]


class bookform(forms.ModelForm):
    class Meta:
        model= booking
        fields= ["eventname","c1","c2","c3","c4","c5",]


class bookform2(forms.ModelForm):
    class Meta:
        model= booking
        fields= ["eventname","c1","c2","c3","c4","c5","user","eventdate",]


class feedform(forms.ModelForm):
    class Meta:
        model= suggestions
        fields= ["text",]


class loginform(forms.ModelForm):
    class Meta:
        model= user
        fields= ["name","password",]
