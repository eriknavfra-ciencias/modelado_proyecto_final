from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm
from django.shortcuts import get_object_or_404

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "agenda/lista.html", {"tareas": tareas})

def nueva_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_tareas")
    else:
        form = TareaForm()
    return render(request, "agenda/nueva.html", {"form": form})

def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = True
    tarea.save()
    return redirect("lista_tareas")

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect("lista_tareas")

