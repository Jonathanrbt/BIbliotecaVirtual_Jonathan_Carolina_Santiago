import json

def reporte():
    report = leer_json

    codigo = report["codigo"]
    titulo_lib = report["titulo"]
    sinopsis = report["sinopsis"]
    autor = report["autor"]
    fecha_publ = report["fecha"]
    cantidades = report["cantidad"]

    for codigo in report.items():
        report.append({
            "Codigo": codigo,


        }) 