from django.conf import settings 
from django.db import models 
from django.utils import timezone

class task(models.Model): 
    nombre = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    descripcion = models.CharField(max_length=200) 
    realizacion = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.nombre 
    