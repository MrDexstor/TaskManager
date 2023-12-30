"""    Проверка выполнения(Выполено, Обновлено)
	Удалена
	Проверяется(Удалено, Новое, Вернуть отправителю)
	Обновлено(В работе, Вернуть отправителю)
	Вернуть отправителю(Обновлено, Удалена)
	Выполнено
	В работе(Проверка выполнения, Вернуть отправителю)
	Новое(В работе)
	
	"""
from main.models import Task
from task.models import task_state
def getButtons(task_id):
    iter = Task.objects.get(id=task_id)
    state = str(iter.state.id)
    if state == '1' :
        action = task_state.objects.filter(id='2')
    elif state == '2':
        action1 = task_state.objects.filter(id='8')
        action2 = task_state.objects.filter(id='4')
        action = action1 | action2
    elif state == '4':
        action1 = task_state.objects.filter(id='5')
        action2 = task_state.objects.filter(id='7')
        action = action1 | action2
    elif state == '5':
        action1 = task_state.objects.filter(id='2')
        action2 = task_state.objects.filter(id='4')
        action = action1 | action2
    elif state == '6':
        action1 = task_state.objects.filter(id='7')
        action2 = task_state.objects.filter(id='1')
        action3 = task_state.objects.filter(id='4')
        action = action1 | action2 | action3
    elif state == '8':
        action1 = task_state.objects.filter(id='3')
        action2 = task_state.objects.filter(id='5')
        action = action1 | action2
    else:
        action = None
    return action
    