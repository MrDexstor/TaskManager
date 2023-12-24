from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import Task
from task.forms import TaskRegisterForm


# Create your views here.
@login_required
def main(request):
    task = Task.objects.order_by('date')[:5]
    return render(request, 'task/index.html', {'task': task})


def task_create(request):
    if request.method == 'POST':
        form = TaskRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_dashboard')
    form = TaskRegisterForm()
    return render(request, 'task/create.html', {'form': form})