from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import Records

class Registerform(UserCreationForm):
    email=forms.EmailField(required=True)
    first_name=forms.CharField(max_length=100,required=True)
    last_name=forms.CharField(max_length=100,required=True)
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')


class CustomerForm(forms.ModelForm):
    first_name=forms.CharField(max_length=50,required=True,label='First Name')
    last_name=forms.CharField(max_length=50,required=True,label='Last Name')
    email=forms.EmailField(required=True,label='Email')
    phone=forms.IntegerField(required=True,label='Phone')
    Address=forms.CharField(max_length=200,required=True,label='Address')
    city=forms.CharField(max_length=30,required=True,label='City')
    state=forms.CharField(max_length=30,required=True,label='State')
    zipcode=forms.CharField(max_length=6,required=True,label='ZipCode')
    class Meta:
        model=Records
        exclude=('created_at',)
   



    


#class UpdateForm(forms.Form):


