from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    """Genera un formulario automático basado en el modelo Tarea."""
    
    class Meta:
        # Configuración básica del formulario
        model = Tarea  # Conecta con la base de datos
        fields = ["titulo", "prioridad", "fecha", "descripcion", "etiquetas"]  # Campos a mostrar

        # visual de los inputs
        widgets = {
            # calndario
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            # caja de descripción
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }