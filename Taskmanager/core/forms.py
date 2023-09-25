from django.forms import ModelForm
from django import forms
from .models  import profile ,Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
class TaskForm(ModelForm):
    class Meta:
        model=Task
        exclude=['user','completed']


class ProfilePicUpdateForm(ModelForm):
    profile_picture=forms.ImageField(label="Profile Picture")
    class Meta:
        model=profile
        fields=('profile_picture',)


class RegisterUserForm(UserCreationForm):
    email=forms.CharField()

    class Meta:
        model=User
        fields=('username','email','password1','password2')


class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name')
    