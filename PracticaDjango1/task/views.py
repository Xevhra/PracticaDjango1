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
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .forms import TaskForm
from .models import task






"""class TaskList(View):
    def get(self, request):
        tasks = task.objects.all()        
        form = TaskForm()
        return render(request, "tareas/task_list.html", {'tasks':  tasks, 'form': form})
            
    def post(self, request):
        tasks = task.objects.all()  
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, "tareas/task_list.html", {'tasks':  tasks, 'form': form})"""
        
        
class TaskList(View):
    nombre_template = 'tareas/home.html'
    
    def actualizaTask(self):
        tasks = task.objects.all()
        return tasks
    
    def get(self, request):
        tasks = self.actualizaTask()
        return render(request, self.nombre_template, {'tasks': tasks, 'form': TaskForm()})


class Tarea_descripcion(View):
    template_description = 'tareas/tarea.html'
    
    def get(self, request, pk):
        task_ = get_object_or_404(task, pk=pk)
        return render(request, self.template_description, {'task': task_})


class Tarea_new(View):
    template_description = 'tareas/new.html'
    
    def get(self, request):
        form = TaskForm()
        task_list_instance = TaskList()
        tasks = task_list_instance.actualizaTask()
        return render(request, self.template_description, {'tasks': tasks, 'form': form})
    
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            realizacion = form.cleaned_data['realizacion']
            
            task.objects.create(nombre=nombre, descripcion=descripcion, realizacion=realizacion)
            return redirect('home')
        
        task_list_instance = TaskList()
        tasks = task_list_instance.actualizaTask()
        return render(request, self.template_description, {'tasks': tasks, 'form': form})

    
    
    
    
          
        
        
        


        
        
        
        

    