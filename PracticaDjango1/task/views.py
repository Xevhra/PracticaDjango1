from django.shortcuts import render, redirect
from .models import task
from .forms import TaskForm

def task_list(request):
    tasks = task.objects.all()
    
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form= TaskForm()
    return render(request, 'tareas/task_list.html', {'tasks': tasks, 'form':form})