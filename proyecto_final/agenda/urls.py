from django.urls import path
from . import views

urlpatterns = [
    # Página principal -> Muestra la lista de todas las tareas
    path("", views.lista_tareas, name="lista_tareas"),

    # Formulario -> Muestra la pantalla para crear una tarea nueva
    path("nueva/", views.nueva_tarea, name="nueva_tarea"),

    # rutas que necesitan el id de la tarea para saber cuál completar o eliminar
    path("completar/<int:tarea_id>/", views.completar_tarea, name="completar_tarea"),
    path("eliminar/<int:tarea_id>/", views.eliminar_tarea, name="eliminar_tarea"),
]