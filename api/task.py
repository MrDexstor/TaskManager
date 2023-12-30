from main.models import Task

def update_state(request, id, state):
    task = Task.objects.get(id=id)
    task.state = task_state.objects.get(id=state)
    task.save(update_fields=["state"])
    return redirect('task_dashboard')


def BaseTaskState(request):
    user_id = request.user.id
    base_state = 1
    if user_id == 1 :
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
    if page == 'task_dashboard' :
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
    data = {'task' : final }
    return data