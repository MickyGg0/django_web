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
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)

        except:
            messages.error(request,"User does not exist !!.")

        user=authenticate(request,username=username,password=password)
 
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request,"Username or password does not exist .")


    context={"page":page}        
    return render(request,"core/login_user.html",context)




def logout_user(request):

    logout(request)
    return redirect('login')


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


def user_profile(request):
    user_profile=request.user.profile
    context={"user_profile":user_profile}
    return render(request,"core/profile.html",context)

def profile_update(request):
    form=forms.ProfileUpdateForm(instance=request.user.profile)
    if request.method=="POST":
        form=forms.ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect("user-profile")


    context={"form":form}

    return render(request,"core/update_profile.html",context)










