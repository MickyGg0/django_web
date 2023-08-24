from django.forms import ModelForm
from django import forms
from . import models

class TaskForm(ModelForm):
    class Meta:
        model=models.Task
        fields='__all__'


class SearchForm(forms.Form):
    query=forms.CharField(max_length=50,label='Search')

