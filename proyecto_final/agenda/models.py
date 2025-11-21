# agenda/models.py
from django.db import models

class Tarea(models.Model):
    """
    Representa una tarea dentro de la agenda.
    """

    ETIQUETAS = [
        ("escuela", "Escuela"),
        ("familia", "Familia"),
        ("ocio", "Ocio"),
        ("social", "Social"),
        ("salud", "Salud"),
        ("hogar", "Hogar"),
    ]

    titulo = models.CharField(max_length=200)
    prioridad = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        default=1
    )
    fecha = models.DateField()
    descripcion = models.TextField(blank=True)
    etiquetas = models.CharField(
        max_length=20,
        choices=ETIQUETAS
    )
    completada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} (Prioridad {self.prioridad})"

    def marcar_completada(self):
        self.completada = True
        self.save()
