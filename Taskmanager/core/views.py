from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms 
from .urls import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login_user(request):

    page="login"
    if request.method == 'POST':
        print(request.POST.get('password'))
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        print(username,password)

        try:
            user=User.objects.get(username=username)

        except:
            messages.error(request,"User does not exist !!.")

        user=authenticate(request,username=username,password=password)
        print(user)
 
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request,"Username or password does not exist .")


    context={"page":page}        
    return render(request,"core/login_user.html",context)


def logout_user(request):

    logout(request)
    return redirect('homepage')


def register_user(request):

    form=UserCreationForm()
    context={"form":form}

    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid(): 
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('homepage')
         
        else :
            messages.error(request,"An error occured during registration.")

        
    return render(request,"core/login_user.html",context)



def homepage(request):
    tasks=models.Task.objects.filter(user=request.user.id)
    # tasks=models.Task.objects.all()
    a=len(tasks)
    if a==0:
        a=True
    else:
        a=False
    
    
    context={"tasks":tasks,"a":a}

    return render(request,"core/homepage.html",context)


@login_required(login_url="/login")
def create_task(request):

    form=forms.TaskForm
    if request.method=='POST':
        form=forms.TaskForm(request.POST)
        if form.is_valid:
            form.instance.user=request.user
            form.save()
            return redirect("homepage")

    context={"form":form}

    return render(request,"core/task_form.html",context)



@login_required(login_url="/login")
def view_task(request):
    tasks=models.Task.objects.all()

    context={'tasks':tasks}
    return render(request,"core/view_task.html",context)


@login_required(login_url="/login")
def into_task(request,pk):

    task=models.Task.objects.get(id=pk)
    context={"task":task}
    return render(request,"core/into_task.html",context)


@login_required(login_url="/login")
def delete_task(request,pk):
    task=models.Task.objects.get(id=pk)
    task.delete()
    return redirect("homepage")

def update_task(request,pk):
    task=models.Task.objects.get(id=pk)
    form=forms.TaskForm(instance=task)

    if request.method=="POST":
        form=forms.TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect("homepage")
    context={"form":form}
        
    return render(request,"core/task_form.html",context)









