from django.shortcuts import render
from .models import task

def task_list(request):
    tasks = task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})