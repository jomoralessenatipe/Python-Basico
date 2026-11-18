# LISTA DE REGISTROS DE ALUMNOS

alumnos = [
    {
        "codigo": 1001,
        "nombre": "CARLOS",
        "edad": 20,
        "promedio": 17
    },
    {
        "codigo": 1002,
        "nombre": "ANA",
        "edad": 19,
        "promedio": 18
    },
    {
        "codigo": 1003,
        "nombre": "PEDRO",
        "edad": 21,
        "promedio": 14
    }
]

# RECORRER LOS REGISTROS

for alumno in alumnos:
    print("CODIGO:", alumno["codigo"])
    print("NOMBRE:", alumno["nombre"])
    print("EDAD:", alumno["edad"])
    print("PROMEDIO:", alumno["promedio"])
    print("----------------------")