"""
MATCH .- Utilizarlo >=3.7
"""
opcion = int(input("Ingrese la opcion:"))
match opcion:
    case 1:
        print("Elegiste Registrar")
    case 2:
        print("Elegiste Eliminar")    
    case 3:
        print("Elegiste Actualizar")    
    case _:
        print("Opcion Incorrecta")    