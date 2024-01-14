from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='task_dashboard'),
    path('create/', views.task_create, name="task_create"),
    path('returned/', views.returned_task, name="task_returned"),
    path('base/<int:task_id>', views.task, name="base"),
    path('base/<int:id>/<int:actions>', views.action),
    path('correct_task/', views.corrections_task, name='correct_task')
]
