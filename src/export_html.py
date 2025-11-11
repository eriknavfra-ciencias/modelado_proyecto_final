#!/usr/bin/env python3

from agenda import *
import argparse
from io_json import *

def main():
    agenda = Agenda()

    parser = argparse.ArgumentParser(description="Gestión de tareas de la agenda.")
    parser.add_argument("archivo", nargs="?", default="demo.json",
                        help="Ruta del archivo json donde se guardan las tareas (por defecto: demo.json)")
    args = parser.parse_args()

    agenda.tareas = cargar_agenda_de_json(args.archivo)
    tareas = agenda.listar_tareas(por="prioridad")

    pendientes = [t[1] for t in tareas if not t[1].completada]
    completadas = [t[1] for t in tareas if t[1].completada]

    def generar_tabla(lista, estado):
        if not lista:
            return f"<p style='text-align:center;'>No hay tareas {estado.lower()}s.</p>"

        html = f"""
        <table>
            <thead>
                <tr><th colspan="6">{estado} ({len(lista)})</th></tr>
                <tr>
                    <th>ID</th><th>Título</th><th>Descripción</th>
                    <th>Prioridad</th><th>Etiquetas</th><th>Completada</th>
                </tr>
            </thead>
            <tbody>
        """
        for t in lista:
            etiquetas = ", ".join(t.etiquetas) if t.etiquetas else "—"
            html += f"""
                <tr>
                    <td>{t.id}</td>
                    <td>{t.titulo}</td>
                    <td>{t.descripcion}</td>
                    <td>{t.prioridad}</td>
                    <td>{etiquetas}</td>
                    <td>{'Sí' if t.completada else 'No'}</td>
                </tr>
            """
        html += "</tbody></table>"
        return html

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Estado actual de la Agenda</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <h1>Reporte de Tareas</h1>
        {generar_tabla(pendientes, "Pendiente")}
        {generar_tabla(completadas, "Completada")}
    </body>
    </html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    main()
