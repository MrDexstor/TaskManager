from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import Task
from task.forms import TaskRegisterForm
from api.task import getTask
from api.task import BaseTaskState
from task.models import task_state
from api.generic import getButtons


@login_required
def main(request):
    page = 'task_dashboard'
    return render(request, 'task/index.html', getTask(request, page))


def returned_task(request):
    return render(request, 'task/returned.html', getTask(request, 'returned_task'))


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_dashboard')
    form = TaskRegisterForm()
    perm = BaseTaskState(request)
    return render(request, 'task/create.html', {'form': form, 'perm': perm})


def task(request, task_id):
    state = getButtons(task_id)
    meta = Task.objects.filter(id=task_id)
    return render(request, 'task/meta.html', {'task': meta, 'states': state})


def action(id, action):
    task = Task.objects.get(id=id)
    task.state = task_state.objects.get(id=action)
    task.save(update_fields=["state"])
    return redirect(f'/task/base/{id}')


def corrections_task(request):
    return render(request, 'task/corrections_task.html')
