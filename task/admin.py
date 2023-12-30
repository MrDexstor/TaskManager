from django.contrib import admin

# Register your models here.
from .models import task_state

admin.site.register(task_state)
