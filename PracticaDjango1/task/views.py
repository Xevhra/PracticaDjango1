#from django.shortcuts import render, redirect
#from .models import task
#from .forms import TaskForm

#def task_list(request):
#    tasks = task.objects.all()
#    
#    if request.method == 'POST':
#        form=TaskForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('task_list')
#    else:
#        form= TaskForm()
#    return render(request, 'tareas/task_list.html', {'tasks': tasks, 'form':form})

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import TaskForm
from .models import task


class TaskList(View):
    def get(self, request):
        tasks = task.objects.all()        
        form = TaskForm()
        return render(request, "tareas/task_list.html", {'tasks':  tasks, 'form': form})
            
    def post(self, request):
        tasks = task.objects.all()  
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tareas/task_list')
        return render(request, "tareas/task_list.html", {'tasks':  tasks, 'form': form})