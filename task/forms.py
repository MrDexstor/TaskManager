from django import forms
from main.models import Task
from django import CreationForm


class TaskRegisterForm(CreationForm):
   
    class Meta:
        model = User
        fields = ['name', 'descriptions', 'author', 'executor', 'date']
        
        