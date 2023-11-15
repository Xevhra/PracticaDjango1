from django import forms
"""
from .models import task

class TaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['nombre','descripcion','realizacion']"""
        
class TaskForm(forms.Form):
      nombre = forms.CharField(label="nombre", max_length=100)
      descripcion = forms.CharField(label="descripcion", widget=forms.Textarea)
      realizacion = forms.BooleanField(label="realizacion", required=False)      