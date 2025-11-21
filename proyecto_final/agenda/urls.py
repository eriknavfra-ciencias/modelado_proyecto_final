# agenda/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_tareas, name="lista_tareas"),
    path("nueva/", views.nueva_tarea, name="nueva_tarea"),
]
