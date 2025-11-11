"""
Pruebas unitarias para la clase Agenda y la clase Tarea.

Se utiliza pytest como framework de testing.
Cada prueba valida un aspecto del comportamiento de la agenda:
- Agregar y buscar tareas
- Eliminar tareas
- Completar tareas
- Buscar por caracteres
- Listar tareas con diferentes criterios
"""

import pytest
from src.agenda import Agenda
from src.tarea import Tarea

@pytest.fixture
def tarea_ejemplo():
    """Crea una tarea de ejemplo para reutilizar en las pruebas."""
    return Tarea(
        titulo="Estudiar probabilidad",
        prioridad=3,
        fecha="2025-09-21",
        etiquetas=["escuela"],
        descripcion="Repasar axiomas"
    )

def test_agregar_y_buscar_tarea(tarea_ejemplo):
    """Verifica que una tarea se pueda agregar y luego recuperar por ID."""
    agenda = Agenda()
    agenda.agregar_tarea(tarea_ejemplo)
    assert len(agenda.tareas) == 1
    encontrada = agenda.buscar_tarea(tarea_ejemplo.id)
    assert encontrada.titulo == "Estudiar probabilidad"

def test_eliminar_tarea(tarea_ejemplo):
    """Verifica que una tarea se elimine correctamente de la agenda."""
    agenda = Agenda()
    agenda.agregar_tarea(tarea_ejemplo)
    id_tarea = tarea_ejemplo.id
    agenda.eliminar_tarea(id_tarea)
    assert agenda.buscar_tarea(id_tarea) is None

def test_completar_tarea(tarea_ejemplo):
    """Verifica que una tarea pueda marcarse como completada."""
    agenda = Agenda()
    agenda.agregar_tarea(tarea_ejemplo)
    id_tarea = tarea_ejemplo.id
    agenda.completar_tarea(id_tarea)
    assert agenda.buscar_tarea(id_tarea).completada is True

def test_buscar_por_caracteres(tarea_ejemplo):
    """Verifica que se pueda buscar una tarea por texto en título o descripción."""
    agenda = Agenda()
    agenda.agregar_tarea(tarea_ejemplo)
    encontrada = agenda.buscar_por_caracteres("axiomas")
    assert encontrada is not None
    assert encontrada.titulo == "Estudiar probabilidad"

def test_listar_tareas_por_prioridad():
    """Verifica que las tareas se ordenen correctamente por prioridad."""
    t1 = Tarea("Tarea baja", 1, "2025-09-21", ["hogar"])
    t2 = Tarea("Tarea alta", 5, "2025-09-21", ["escuela"])
    agenda = Agenda()
    agenda.agregar_tarea(t1)
    agenda.agregar_tarea(t2)
    ordenadas = agenda.listar_tareas("prioridad")
    assert ordenadas[0][1].titulo == "Tarea alta"
