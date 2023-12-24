form .models import Task
from django.forms import ModelForm, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'executor', 'descriptions', 'date', 'author']
        
        widgets = {
            'name': TextInput(attrs={
                'class' : ''
            }),
            'executor': ForeignKey(attrs={
                'class' : ''
            }),
            'descriptions': TextInput(attrs={
                'class' : ''
            }),
            'date': DateTimeField(attrs={
                'class' : ''
            }),
            'author': ForeignKey(attrs={
                'class' : ''
            })
 
 
        }