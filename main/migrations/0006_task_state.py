# Generated by Django 5.1.dev20231201130304 on 2023-12-25 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_task_author'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='state',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='Состояние', to='task.task_state'),
        ),
    ]
