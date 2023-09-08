from django.forms import ModelForm
from django import forms
from . import models

class TaskForm(ModelForm):
    class Meta:
        model=models.Task
        exclude=['user']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model=models.profile
        fields="__all__"


 

 

   