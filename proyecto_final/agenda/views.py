from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm

def lista_tareas(request):
    """Vista principal: Muestra todas las tareas guardadas."""
    tareas = Tarea.objects.all()  # Saca todas las tareas de la base de datos
    return render(request, "agenda/lista.html", {"tareas": tareas})

def nueva_tarea(request):
    """Maneja el formulario para crear una tarea nueva."""
    if request.method == "POST":
        # Si el usuario mandó datos, se guardan
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_tareas") # Nos regresa a la lista
    else:
        # Si apenas entró a la página, le mostramos el formulario vacío
        form = TareaForm()
    return render(request, "agenda/nueva.html", {"form": form})

def completar_tarea(request, tarea_id):
    """Busca una tarea por su ID y la marca como lista."""
    tarea = get_object_or_404(Tarea, id=tarea_id) # Si no existe, da error 
    tarea.completada = True
    tarea.save() # Guarda el cambio en la base de datos
    return redirect("lista_tareas")

def eliminar_tarea(request, tarea_id):
    """Busca una tarea por su ID y la borra para siempre."""
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete() # La elimina de la base de datos
    return redirect("lista_tareas")