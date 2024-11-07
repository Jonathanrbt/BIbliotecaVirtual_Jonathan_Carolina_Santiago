import json


def leer_json(archivo):
    try:
        with open(archivo, 'r') as file_libros:
            return json.load(file_libros)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}




def escribir_json(datos, archivo):
    with open(archivo, 'w') as file_libros:
        json.dump(datos, file_libros, indent=4)