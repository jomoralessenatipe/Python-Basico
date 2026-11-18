"""
REGISTROS .- PERMITEN ALMACENAR DIFERENTES DATOS
RELACIONADOS A UNA MISMA ENTIDAD.

EJEMPLO: REGISTRO ALUMNO
CAMPOS:
- CODIGO
- NOMBRE
- EDAD
- CARRERA
- PROMEDIO
"""

alumno = {
    "codigo": 1001,
    "nombre": "CARLOS",
    "edad": 20,
    "carrera": "INGENIERIA DE SISTEMAS",
    "promedio": 17.5
}

print(alumno)

# ACCEDER A UN CAMPO DEL REGISTRO

print(alumno["codigo"])
print(alumno["nombre"])
print(alumno["edad"])
print(alumno["carrera"])
print(alumno["promedio"])

# ACTUALIZAR UN CAMPO

alumno["nombre"] = "PEDRO"
alumno["edad"] = 22
alumno["promedio"] = 18.5

print(alumno)

# AGREGAR UN NUEVO CAMPO

alumno["ciclo"] = 5
alumno["estado"] = "REGULAR"

print(alumno)

# ELIMINAR UN CAMPO

alumno.pop("estado")

print(alumno)

# RECORRER EL REGISTRO

for campo, valor in alumno.items():
    print(campo, ":", valor)