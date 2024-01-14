from django.contrib import admin
from .models import Permission
from .models import UserPermissions
# Register your models here.
admin.site.register(Permission)
admin.site.register(UserPermissions)