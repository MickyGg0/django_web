from django.forms import ModelForm
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(ModelForm):
    class Meta:
        model=models.Task
        exclude=['user','completed']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model=models.profile
        exclude=["user"]


class RegisterUserForm(UserCreationForm):
    first_name=forms.CharField()
    last_name=forms.CharField()

    class Meta:
        model=User
        fields=('username','first_name','last_name','password1','password2')



 

 

   