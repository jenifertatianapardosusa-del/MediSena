"""Capa de persistencia: lectura y escritura del archivo data/citas.json."""

import json
import os

RUTA_ARCHIVO = os.path.join("data", "citas.json")


def cargar_citas() -> list:
    """Lee el archivo JSON y devuelve una lista de diccionarios."""
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("Aviso: no existe data/citas.json. Se iniciara con una lista vacia.")
        return []
    except json.JSONDecodeError:
        print("Error: el archivo JSON esta corrupto. Se iniciara con una lista vacia.")
        return []


def guardar_citas(citas: list) -> None:
    """Escribe la lista de citas en el archivo JSON."""
    os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(citas, archivo, indent=4, ensure_ascii=False)
