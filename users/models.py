from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Permission(models.Model):

    permission = models.TextField('Право')

    def __str__(self):
        return self.permission

    class Meta:
        verbose_name = 'Право'
        verbose_name_plural = 'Права'


class UserPermissions(models.Model):
    object = None
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name='Право')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Пользователь')

    def __str__(self):
        names = f'{self.user} - {self.permission}'
        return names

    class Meta:
        verbose_name = 'Наследование'
        verbose_name_plural = 'Наследование прав'
