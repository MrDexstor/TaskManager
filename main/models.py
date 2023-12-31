from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from task.models import task_state


class Task(models.Model):
    objects = None
    name = models.CharField('Название задачи', max_length=100)
    executor = models.ForeignKey(User, default="1", on_delete=models.CASCADE, related_name='executor')
    descriptions = models.TextField('Описание задачи')
    date = models.DateTimeField('Дата публикации', default=timezone.now)
    author = models.ForeignKey(User, default="1", on_delete=models.CASCADE, related_name='Автор')
    state = models.ForeignKey(task_state, default="1", on_delete=models.CASCADE, related_name='Состояние')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'
