from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import Registerform,CustomerForm
from django.contrib.auth.decorators import login_required
from . models import Records

# Create your views here.
def home(request):
    if(request.method=='POST'):
        username=request.POST['un']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if(user is not None):
            login(request,user)
            messages.success(request,'you are successfully logged in !')
            return redirect('home')
        else:
            messages.error(request,'credentials did not match try again!')
            return redirect('home')
    if(request.user.is_authenticated):
        records=Records.objects.all()
        return render(request,'home.html',{'records':records})
    
    


def logout_user(request):
    logout(request)
    messages.success(request,'you are successfully loggedout !')
    return redirect('home')

def register(request):
    form=Registerform()
    if(request.method=='POST'):
        form=Registerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'your account has been created please login!')
            return redirect('home')
        else:
            context={
            'form':form
            }
            return render(request,'register.html',context)
    
        
    else:
        context={
            'form':form
        }
        return render(request,'register.html',context)
    
@login_required(login_url='home')
def createcustomer(request):
    form=CustomerForm()
    if(request.method=='POST'):
        form=CustomerForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request,'Customer created Sucessfully')
            return redirect('home')
    return render(request,'customerform.html',{'form':form})

@login_required(login_url='home')
def update(request,pk):
    current_record=Records.objects.get(id=pk)
    form=CustomerForm(instance=current_record)
    if(request.method=='POST'):
        form=CustomerForm(request.POST,instance=current_record)
        if(form.is_valid()):
            form.save()
            messages.success(request,'Data Updated Successfully !')
            return redirect('home')
    
    return render(request,'update.html',{'form':form,'current_record':current_record})
    

@login_required(login_url='home')
def select(request,id):
    r=Records.objects.get(id=id)
    return render(request,'select.html',{'record':r})


@login_required(login_url='home')
def delete(request,pk):
    r=Records.objects.get(id=pk)
    if(request.method=='POST'):
        final=request.POST['final']
        if(final=='YES'):
            r=Records.objects.get(id=pk)
            r.delete()
            messages.success(request,'Record deleted Sucessfully!')
            return redirect('home')
        elif(final=='NO'):
            return redirect('home')
        else:
            messages.error(request,'Enter correctly as shown the field!')
        
    return render(request,'delete.html',{'record':r})
    



    
    