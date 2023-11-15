from django.urls import path
from . import views
from .views import TaskList, Tarea_descripcion, Tarea_new

urlpatterns = [
    path('', TaskList.as_view(), name='home'),
    path('tarea/<int:pk>', Tarea_descripcion.as_view(), name='tarea'),
    path('tarea/new', Tarea_new.as_view(), name="new")  
    
]