# agenda/forms.py
from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ["titulo", "prioridad", "fecha", "descripcion", "etiquetas", "completada"]
