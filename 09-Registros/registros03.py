alumnos = []

# REGISTRAR 3 ALUMNOS
for i in range(3):

    print("REGISTRO DE ALUMNO", i + 1)

    alumno = {
        "codigo": int(input("Ingrese código: ")),
        "nombre": input("Ingrese nombre: "),
        "promedio": float(input("Ingrese promedio: "))
    }

    alumnos.append(alumno)

# MOSTRAR REGISTROS
print("\nLISTA DE ALUMNOS")

for alumno in alumnos:

    print("CODIGO:", alumno["codigo"])
    print("NOMBRE:", alumno["nombre"])
    print("PROMEDIO:", alumno["promedio"])

    if alumno["promedio"] >= 11:
        print("ESTADO: APROBADO")
    else:
        print("ESTADO: DESAPROBADO")

    print("-------------------")