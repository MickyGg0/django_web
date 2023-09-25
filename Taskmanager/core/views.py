# Import statements
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Import local modules
from . import forms
from . import models
from .urls import *

# Login View

def login_user(request):
    page = "login"
    
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User does not exist!!")
            user = None

        if user:
            user = authenticate(request, username=username, password=password, email=email)
            
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, "Username or password does not exist.")

    context = {"page": page}        
    return render(request, "core/login_user.html", context)

# Logout View
@login_required(login_url='/')
def logout_user(request):
    logout(request)
    return redirect('login')

# User Registration View
def register_user(request):
    form = forms.RegisterUserForm()
    context = {"form": form}

    if request.method == 'POST':
        form = forms.RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, "An error occurred during registration.")

    return render(request, "core/login_user.html", context)

# Homepage View
@login_required(login_url="/")
def homepage(request):
    completed_tasks = []
    not_completed_tasks = []


    profile=request.user.profile.profile_picture.url
    


    
    tasks = models.Task.objects.filter(user=request.user.id)
    
    for task in tasks:
        if task.completed:
            completed_tasks.append(task)
        else:
            not_completed_tasks.append(task)
    
    a = len(not_completed_tasks)
    b = len(completed_tasks)

    if b>0:
        b==True
    else:
        b==False
    
    context = {"a": a, "tasks_b": completed_tasks, "tasks_a": not_completed_tasks,"profile":profile}
    
    return render(request, "core/homepage.html", context)

# Task Creation View

def create_task(request):
    form = forms.TaskForm()
    print("prefill")

    if request.method=='POST':
        form = forms.TaskForm(request.POST)
        print("post")
        
        try:
            if form.is_valid():
                print("valid form")
                form.instance.user = request.user
                form.save()
                print("done")
                return redirect("homepage")

        except ValueError:
            messages.error(request, "Please check your entries and try again!")

    context = {"form": form}
    return render(request, "core/task_form.html", context)

# Task Deletion View
@login_required(login_url='/')
def delete_task(request, pk):
    task = models.Task.objects.get(id=pk)
    task.delete()
    return redirect("homepage")

# Task Update View
@login_required(login_url='/')
def update_task(request, pk):
    task = models.Task.objects.get(id=pk)
    form = forms.TaskForm(instance=task)
    name=task.name
    priority=task.priority
    due_date=task.due_date
    description=task.description

    if request.method =="POST":
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("homepage")
    
    context = {"form": form,"name":name,"priority":priority,"due_date":due_date,"description":description}
    return render(request, "core/task_form.html", context)

# User Profile View
@login_required(login_url='/')
def user_profile(request):
    user_profile = request.user.profile
    context = {"user_profile": user_profile}
    print(user_profile.profile_picture)
    return render(request, "core/profile.html", context)



# Task Completion View
@login_required(login_url='/')
def complete_task(request, pk):
    task_complete = models.Task.objects.get(id=pk)
    task_complete.completed = True
    task_complete.save()
    return redirect("homepage")

# Task Restoration View
@login_required(login_url='/')
def restore_task(request, pk):
    task_restore = models.Task.objects.get(id=pk)
    task_restore.completed = False
    task_restore.save()
    return redirect("homepage")


@login_required(login_url='/')
def update_profile(request):
    form1=forms.ProfileUpdateForm(instance=request.user)
    form2=forms.ProfilePicUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    if request.method=="POST":  
        form1=forms.ProfileUpdateForm(instance=request.user)
        form2=forms.ProfilePicUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()     
    context={"form1":form1,"form2":form2}


    return render(request,"core/profile.html",context)