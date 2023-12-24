from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='task_dashboard'),
    path('create/', views.task_create, name="create")
]
