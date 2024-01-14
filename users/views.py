from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile():
    pass


def logout_user(request):
    logout(request)
    return redirect('/')
