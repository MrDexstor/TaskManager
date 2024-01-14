from django.shortcuts import redirect, render
from main.models import Task
from task.models import task_state
from users.models import UserPermissions
from users.models import Permission
from django.contrib.auth.models import User
from api.permissions import checkAccept


def BaseTaskState(request):
    permission = 'task.create.default_new'
    accept = checkAccept(request, permission)
    if accept == True:
        base_state = 1
    else:
        base_state = 6
    return base_state


def getUserFilteredTask(user, state_id):
    return Task.objects.filter(executor=user, state=state_id)


def getReturnedTask(user):
    return Task.objects.filter(author=user, state='4')


def getTask(request, page):
    user = request.user.id
    if page == 'task_dashboard':
        task_working = getUserFilteredTask(user, '2')
        task_returned = getReturnedTask(user)
        task_new = getUserFilteredTask(user, '1')
        final = task_returned | task_new | task_working
    elif page == 'main':
        task_returned = getReturnedTask(user)
        final = task_returned
    elif page == 'returned_task':
        task_returned = getReturnedTask(user)
        final = task_returned
    else:
        final = None
    data = {'task': final}
    return data


def getCorrectionsTask(request):
    user = request.user.id
    first = getTaskForCorrecting(request)
    second = Task.objects.filter(author=user, state='6')
    data = {'first': first, 'second': second}
    return data


def getTaskForCorrecting(request):
    prefix = 'task.correcting.from.'
    permissions = Permission.objects.filter(permission__startswith=prefix)
    user_permissions = UserPermissions.objects.filter(permission__in=permissions, user=request.user)
    array = []
    for user_perm in user_permissions:
        permission_text = user_perm.permission.permission
        if permission_text.startswith(prefix):
            text_after_prefix = permission_text[len(prefix):]
            array.append(text_after_prefix)
    final = Task.objects.filter(author__username__in=array, state='6')
    return final


def update_state(id, state):
    task = Task.objects.get(id=id)
    task.state = task_state.objects.get(id=state)
    task.save(update_fields=["state"])
    return redirect('task_dashboard')