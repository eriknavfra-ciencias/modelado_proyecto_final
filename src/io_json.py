import uuid
from tarea import Tarea
import json

def serializar(tarea: Tarea) -> dict | None:
    """
    Convierte una instancia de Tarea en un diccionario serializable a JSON.
    """
    if isinstance(tarea, Tarea):
        return {
            "id": str(tarea.id),
            "titulo": tarea.titulo,
            "prioridad": tarea.prioridad,
            "fecha": tarea.fecha.strftime("%Y-%m-%d"),
            "descripcion": tarea.descripcion,
            "etiquetas": tarea.etiquetas,
            "completada": tarea.completada
        }
    return None

def cargar_agenda_de_json(nombre_archivo: str) -> dict[str, Tarea]:
    """
    Carga una agenda desde un archivo JSON y devuelve un diccionario de tareas.
    """
    try:
        with open(nombre_archivo, "r") as archivo:
            datos = json.load(archivo)
        agenda = {}
        for tarea_dict in datos["tareas"]:
            tarea = Tarea(
                tarea_dict["titulo"],
                tarea_dict["prioridad"],
                tarea_dict["fecha"],
                tarea_dict["etiquetas"],
                tarea_dict["descripcion"],
                tarea_dict["completada"]
            )
            tarea.id = str(uuid.UUID(tarea_dict["id"]))
            agenda[tarea.id] = tarea
        return agenda

    except FileNotFoundError as fnfe:
        print(f"Error al cargar la agenda: {fnfe}")
        return {}

    except json.JSONDecodeError as jde:
        print(f"Error al cargar la agenda: {jde}")
        return {}

def guardar_agenda(tareas: dict[str, Tarea], nombre_archivo: str):
    """
    Guarda las tareas en un archivo JSON.
    """
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump({"tareas": list(tareas.values())}, archivo,
                      indent=4, ensure_ascii=False, default=serializar)
            print(f"Agenda guardada correctamente en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar la agenda: {e}")
