from django.db import models

class Tarea(models.Model):
    """Define la estructura de la tabla 'Tarea' en la base de datos."""

    # Lista de opciones fijas para clasificar tareas
    ETIQUETAS = [
        ("escuela", "Escuela"),
        ("familia", "Familia"),
        ("ocio", "Ocio"),
        ("social", "Social"),
        ("salud", "Salud"),
        ("hogar", "Hogar"),
    ]

    # definimos columnas
    titulo = models.CharField(max_length=200) 
    prioridad = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], # permite del 1 al 5
        default=1
    )
    fecha = models.DateField()  # Fecha de entrega
    descripcion = models.TextField(blank=True)  # texto largo
    etiquetas = models.CharField(
        max_length=20,
        choices=ETIQUETAS  # usa la lista de arriba
    )
    completada = models.BooleanField(default=False) # inicia siempre como pendiente

    def __str__(self):
        # Texto que muestra Django en el panel de administración
        return f"{self.titulo} (Prioridad {self.prioridad})"

    def marcar_completada(self):
        # Función para actualizar el estado
        self.completada = True
        self.save()