from django.conf import settings 
from django.db import models 
from django.utils import timezone
from django import forms

class task(models.Model): 
    nombre = models.CharField(max_length=200) 
    descripcion = models.CharField(max_length=500) 
    realizacion = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.nombre

    
    
  
    