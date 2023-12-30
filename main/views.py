from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    task = Task.objects.filter(state="4", author=request.user.id)
    return render(request, 'main/dashboard.html', {'task': task})