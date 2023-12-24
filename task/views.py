from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Task
# Create your views here.
@login_required
def main(request):
    task = Task.objects.order_by('date')[:5]
    return render(request, 'task/index.html', {'task': task})