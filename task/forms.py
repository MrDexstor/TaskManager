from django.forms import ModelForm, TextInput, DateTimeInput
from main.models import Task


class TaskRegisterForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'descriptions', 'executor']

        widgets={
            'name': TextInput(attrs={
                'class': '',

            }),
            'descriptions': TextInput(attrs={
                'class': '',

            })
        }