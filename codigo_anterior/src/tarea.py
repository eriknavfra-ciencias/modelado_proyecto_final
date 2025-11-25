from datetime import datetime

class Tarea:
    """
    Representa una tarea dentro de la agenda.

    Atributos:
        id (str | None): Identificador único de la tarea (UUID en forma de string).
        titulo (str): Título de la tarea.
        prioridad (int): Nivel de prioridad (1 = baja, 5 = alta).
        fecha (datetime): Fecha límite de la tarea en formato YYYY-MM-DD.
        descripcion (str): Descripción detallada de la tarea.
        etiquetas (list[str]): Lista de etiquetas válidas asociadas a la tarea.
        completada (bool): Estado de la tarea (True si está completada).
    """

    ETIQUETAS = ["escuela", "familia", "ocio", "social", "salud", "hogar"]

    def __init__(self, titulo: str, prioridad: int,
                 fecha: str, etiquetas: list[str], descripcion: str = "",
                 completada: bool = False):
        """
        Inicializa una nueva tarea validando prioridad, fecha y etiquetas.

        Args:
            titulo (str): Título de la tarea.
            prioridad (int): Número entre 1 y 5 que indica la prioridad.
            fecha (str): Fecha en formato 'YYYY-MM-DD'.
            etiquetas (list[str]): Lista de etiquetas válidas.
            descripcion (str, opcional): Texto descriptivo de la tarea.
            completada (bool, opcional): Estado inicial de la tarea.
        """
        self.id: str | None = None
        self.titulo = titulo

        if not 1 <= prioridad <= 5:
            raise ValueError("Prioridad fuera del rango valido [1,5]")
        self.prioridad = prioridad

        try:
            self.fecha = datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            raise ValueError("La fecha no esta en el formato correcto (aaaa-mm-dd)")

        # Filtra etiquetas inválidas
        self.descripcion = descripcion
        self.etiquetas = [e.lower().strip() for e in etiquetas if e.lower().strip() in self.ETIQUETAS]
        self.completada = completada

    def __str__(self) -> str:
        """Devuelve una representación legible de la tarea."""
        s = f"Tarea: {self.titulo}\n"
        s += f"ID: {self.id if self.id is not None else 'N/A'}\n"
        s += f"Prioridad: {self.prioridad}\n"
        s += f"Fecha: {self.fecha.strftime('%Y-%m-%d')}\n"
        s += f"Descripcion: {self.descripcion}\n"
        s += f"Etiquetas: {', '.join(self.etiquetas)}\n"
        s += f"Completada: {'Sí' if self.completada else 'No'}\n"
        return s

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.completada = True

    def __lt__(self, other):
        """Permite comparar tareas por prioridad (para ordenación)."""
        if not isinstance(other, Tarea):
            return NotImplemented
        return self.prioridad < other.prioridad

    def __eq__(self, other):
        """Dos tareas son iguales si comparten el mismo ID."""
        if not isinstance(other, Tarea):
            return NotImplemented
        return self.id is not None and self.id == other.id
