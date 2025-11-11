import uuid
from tarea import Tarea

class Agenda:
    """
    Clase que gestiona un conjunto de tareas.

    Métodos principales:
        agregar_tarea: Añade una nueva tarea a la agenda.
        eliminar_tarea: Elimina una tarea por ID.
        buscar_tarea: Devuelve una tarea por ID.
        completar_tarea: Marca una tarea como completada.
        buscar_por_caracteres: Busca una tarea por texto en título o descripción.
        listar_tareas: Devuelve las tareas ordenadas por un criterio.
    """

    def __init__(self):
        """Inicializa la agenda con un diccionario vacío de tareas."""
        self.tareas: dict[str, Tarea] = {}
        self.contador = 1

    def agregar_tarea(self, tarea: Tarea) -> None:
        """Agrega una tarea nueva generando un UUID único."""
        if tarea.id is not None and tarea.id in self.tareas:
            print(f"Advertencia: La tarea ya tiene un ID y está en la agenda.")
            return

        nuevo_id = str(uuid.uuid4())
        tarea.id = nuevo_id
        self.tareas[nuevo_id] = tarea
        self.contador += 1
        print(f"Tarea '{tarea.titulo}' agregada con éxito con ID: {nuevo_id}")

    def eliminar_tarea(self, id: str) -> None:
        """Elimina una tarea por ID si existe."""
        if id in self.tareas:
            del self.tareas[id]
            print(f"Tarea con ID {id} eliminada.")
        else:
            print(f"Tarea con ID {id} no encontrada.")

    def buscar_tarea(self, id: str) -> Tarea | None:
        """Busca una tarea por ID y la devuelve si existe."""
        return self.tareas.get(id)

    def completar_tarea(self, id: str) -> None:
        """Marca como completada la tarea con el ID dado."""
        t = self.buscar_tarea(id)
        if t:
            t.marcar_completada()
            print(f"Tarea '{t.titulo}' marcada como completada.")
        else:
            print(f"Tarea con id {id} no encontrada.")

    def buscar_por_caracteres(self, identificador: str) -> Tarea | None:
        """Busca la primera tarea que contenga el texto en título o descripción."""
        for tarea in self.tareas.values():
            if identificador in tarea.descripcion or identificador in tarea.titulo:
                return tarea
        return None

    def listar_tareas(self, por: str = "id") -> list[tuple[str, Tarea]]:
        """
        Lista todas las tareas ordenadas por un criterio.

        Args:
            por (str): Criterio de ordenación ("id", "prioridad", "fecha", "titulo").
        """
        items = self.tareas.items()
        if por == "prioridad":
            return sorted(items, key=lambda item: item[1].prioridad, reverse=True)
        elif por == "fecha":
            return sorted(items, key=lambda item: item[1].fecha)
        elif por == "titulo":
            return sorted(items, key=lambda item: item[1].titulo)
        else:  # "id"
            return sorted(items)
