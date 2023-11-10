from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import MyForm


class myview(View):
    def get(request, self):
        tasks = Task.objects.all()        
        form = TaskForm(request.POST)
        return render(request, "tarea/task_list.html", {'tarea':  self.task, 'form': form})
            
    def post(request, self):
        form = TaskForm(request.post)
        if form.is_valid():
            form.save()
        return redirect('task_list')

        