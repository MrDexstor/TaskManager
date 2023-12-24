from django.forms import TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        password = TextInput
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name@example.com',
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'name@example.com',
            }),
            "password1": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'name@example.com',
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'name@example.com',
            })

        }
