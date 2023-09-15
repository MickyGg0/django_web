from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms 
from .urls import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
import os,os.path
from django.conf  import settings
from django.views.decorators.cache import cache_control
# Create your views here.
def login_user(request):
    page="login"
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        try:
            user=User.objects.get(username=username)

        except:
            messages.error(request,"User does not exist !!.")

        user=authenticate(request,username=username,password=password,eamil=email)
 
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

    form=forms.RegisterUserForm()
    context={"form":form}

    if request.method=='POST':
        form=forms.RegisterUserForm(request.POST)
        if form.is_valid(): 
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('homepage')
         
        else :
            messages.error(request,"An error occured during registration.")

        
    return render(request,"core/login_user.html",context)


@login_required(login_url="/")
def homepage(request):
    completed_tasks=[]
    not_completed_tasks=[]

    tasks=models.Task.objects.filter(user=request.user.id)

    for task in tasks:
        if task.completed==True:
            completed_tasks.append(task)
        else:
            not_completed_tasks.append(task)
    print(completed_tasks)
    print(not_completed_tasks)


    b=len(completed_tasks)
    if b>0:
        b=True
    else:
        b=False
    print(b)


    a=len(not_completed_tasks)
    print(a)

    if a>0:
        a=True
    else:
        a=False
    print(a)

    context={"a":a,"tasks_b":completed_tasks,"tasks_a":not_completed_tasks}

    return render(request,"core/homepage.html",context)


@login_required(login_url="/")
def create_task(request):

    form=forms.TaskForm
    if request.method=='POST':
        try:
            form=forms.TaskForm(request.POST)
            if form.is_valid:
                form.instance.user=request.user
                form.save()
                return redirect("homepage")
        except ValueError:
            messages.error(request,"Pls check your entries and try agian !!!")

    context={"form":form}

    return render(request,"core/task_form.html",context)






@login_required(login_url="/")
def into_task(request,pk):

    task=models.Task.objects.get(id=pk)
    context={"task":task}
    return render(request,"core/into_task.html",context)


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
    updating_profile=True
    form=forms.ProfileUpdateForm(instance=request.user.profile)
    if request.method=="POST":

        form=forms.ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        # user's current profile picture.
        old_profile_pic=(request.user.profile.profile_picture.path)
        print(old_profile_pic)
        old_picture_path=(os.path.join(settings.MEDIA_ROOT,(old_profile_pic)))
        print(old_profile_pic)

        if form.is_valid():
            try:
                if os.path.exists((old_picture_path)):
                    os.remove((old_picture_path))    
            except:
                pass

            form.save()
            return redirect("user-profile")


    context={"form":form,"updating_profile":updating_profile}

    return render(request,"core/profile.html",context)



def edit_profile(request):
    print(request.user.username)
    print(request.user.first_name)
    print(request.user.last_name)
    form=forms.RegisterUserForm(request.user)
    if request.method=="POST":
        form=forms.RegisterUserForm(request.POST,instance=form)
        
        
    return render(request,"core/edit-profile.html")



def complete_task(request,pk):
    task_complete=models.Task.objects.get(id=pk)
    task_complete.completed=True
    task_complete.save()
    print(task_complete.completed)
    return redirect("homepage")

def restore_task(request,pk):
    task_restore=models.Task.objects.get(id=pk)
    task_restore.completed=False
    task_restore.save()

    return redirect("homepage")