from django.db import models


# Create your models here.
class task_state(models.Model):
    objects = None
    name = models.CharField('Состояние', max_length=100)
    meta_info = models.CharField('Мета-информация', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния задач'
