import json
import os 

# Funciones para la gestión de usuarios con JSON

def cargar_usuarios(): #Json
    if os.path.exists(archivo_usuarios):
        with open(archivo_usuarios, "r", encoding="utf-8") as file:
            return json.load(file)
    return []  # Retorna una lista vacía si el archivo no existe

def guardar_usuarios(usuarios): #Json
    with open(archivo_usuarios, "w", encoding="utf-8") as file:
        json.dump(usuarios, file, indent=4)  # Usa indent=4 para una mejor legibilidad

