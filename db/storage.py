import json
import os 
from datetime import datetime

DATA_DIR = "static/"

def load_data(filename):
    """Carga datos desde un archivo JSON ubicado en el directorio estático.

    Args:
        filename (str): Nombre del archivo JSON a cargar.

    Returns:
        list | dict: Datos cargados del archivo JSON. Si el archivo no existe,
        retorna una lista vacía.
    """
    path = DATA_DIR + filename
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return []


def save_data(data, filename):
    """Guarda datos en un archivo JSON en el directorio estático.

    Args:
        data (list | dict): Estructura de datos a guardar (ej. lista o diccionario).
        filename (str): Nombre del archivo JSON de destino.

    Returns:
        None
    """
    path = DATA_DIR + filename
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

