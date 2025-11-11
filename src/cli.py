#!/usr/bin/env python3
"""
Módulo principal de la aplicación Agenda.

Este archivo define la interfaz de línea de comandos (CLI) para gestionar tareas.
Permite agregar, listar, completar, eliminar, buscar, guardar y cargar tareas
desde un archivo JSON.

Uso:
    agenda add --titulo "..." --descripcion "..." --prioridad 3 --fecha 2025-09-21 --etiquetas escuela
    agenda ls --por prioridad
    agenda done <ID>
    agenda rm <ID>
    agenda find "texto"
    agenda save demo.json
    agenda load demo.json
"""

import argparse
from datetime import datetime

from agenda import Agenda
from io_json import *

def main():
    """
    Función principal que inicializa la agenda y procesa los comandos de la CLI.
    """
    agenda = Agenda()

    # Parser principal
    parser = argparse.ArgumentParser(description="Gestión de tareas de la agenda.")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles", required=True)

    # -------------------------
    # Subcomando: add
    # -------------------------
    parser_agregar = subparsers.add_parser("add", help="Agregar una nueva tarea")
    parser_agregar.add_argument("--titulo", help="Título de la tarea")
    parser_agregar.add_argument("--descripcion", help="Descripción de la tarea")
    parser_agregar.add_argument("--prioridad", type=int, default=1, help="Prioridad de la tarea (1-5)")
    parser_agregar.add_argument("--fecha", default=datetime.now().strftime('%Y-%m-%d'),
                                help="Fecha de la tarea (YYYY-MM-DD)")
    parser_agregar.add_argument("--etiquetas", default="escuela", nargs='+',
                                help="Una o más etiquetas (ej: escuela hogar)")

    # -------------------------
    # Subcomando: ls
    # -------------------------
    parser_listar = subparsers.add_parser("ls", help="Listar todas las tareas")
    parser_listar.add_argument("--por", choices=["prioridad", "fecha", "titulo"], default="id",
                               help="Criterio de ordenación")

    # -------------------------
    # Subcomando: done
    # -------------------------
    parser_completar = subparsers.add_parser("done", help="Marcar una tarea como completada")
    parser_completar.add_argument("id", help="ID de la tarea a completar")

    # -------------------------
    # Subcomando: rm
    # -------------------------
    parser_eliminar = subparsers.add_parser("rm", help="Eliminar una tarea")
    parser_eliminar.add_argument("id", help="ID de la tarea a eliminar")

    # -------------------------
    # Subcomando: find
    # -------------------------
    parser_buscar = subparsers.add_parser("find", help="Encuentra una tarea por título o descripción")
    parser_buscar.add_argument("identificador", help="Texto a buscar")

    # -------------------------
    # Subcomando: save
    # -------------------------
    parser_guardar = subparsers.add_parser("save", help="Guardar la agenda")
    parser_guardar.add_argument("archivo", default="demo.json", help="Nombre del archivo a guardar")

    # -------------------------
    # Subcomando: load
    # -------------------------
    parser_cargar = subparsers.add_parser("load", help="Cargar la agenda")
    parser_cargar.add_argument("archivo", default="demo.json", help="Nombre del archivo a cargar")

    # Parseo de argumentos
    args = parser.parse_args()

    # Archivo por defecto
    guardar = True
    ruta = "./demo.json"
    agenda.tareas = cargar_agenda_de_json(ruta)

    # -------------------------
    # Ejecución de comandos
    # -------------------------
    if args.command == "load":
        if args.archivo:
            ruta = args.archivo
        agenda.tareas = cargar_agenda_de_json(ruta)
        print("Agenda cargada correctamente.")

    if args.command == "add":
        try:
            nueva_tarea = Tarea(
                titulo=args.titulo,
                descripcion=args.descripcion,
                prioridad=args.prioridad,
                fecha=args.fecha,
                etiquetas=args.etiquetas
            )
            agenda.agregar_tarea(nueva_tarea)
        except ValueError as e:
            print(f"Error al crear la tarea: {e}")

    elif args.command == "ls":
        guardar = False
        if not agenda.tareas:
            print("No hay tareas en la agenda.")
        else:
            sorted_tareas = agenda.listar_tareas(args.por)
            for id_tarea, tarea in sorted_tareas:
                print(f"ID: {id_tarea}\n{tarea}")

    elif args.command == "done":
        agenda.completar_tarea(args.id)

    elif args.command == "rm":
        agenda.eliminar_tarea(args.id)

    elif args.command == "find":
        tarea_encontrada = agenda.buscar_por_caracteres(args.identificador)
        if tarea_encontrada:
            print(tarea_encontrada)
        else:
            print(f"No existe una tarea que contenga {args.identificador} en su título o descripción")

    elif args.command == "save":
        if args.archivo:
            ruta = args.archivo

    # Guardar cambios si corresponde
    if guardar:
        guardar_agenda(agenda.tareas, ruta)

if __name__ == "__main__":
    main()
