from modulos_acme.archivos_acme import *



def gestor_libros ():
    arhivo_libros = leer_json('archivos/archivo_libros.json')
    codigo = input('''
╔════════════════════╗
║  REGISTRAR LIBROS  ║
╚════════════════════╝

Ingrese el codigo de su nuevo producto: ''').strip()
    titulo = input('Ingrese el titulo de su nuevo libro: ').strip()
    sinopsis = input('Ingrese la sinopsis de su nuevo libro: ').strip()
    autor = input('Ingrese el autor de su nuevo libro: ').strip()
    anio = input('Ingrese el año de lanzamiento de su libro: ').strip()
    mes = input('Ingrese el mes de lanzamiento de su libro: ').strip()
    dia = input('Ingrese el dia de lanzamiento de su libro: ').strip()