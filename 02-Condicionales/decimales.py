#----------------------------------------------------------
# Decimal permite representar números decimales con mayor precisión 
# que float, especialmente cuando trabajamos con 
# operaciones financieras, dinero, impuestos y cálculos contables.
#----------------------------------------------------------
from decimal import Decimal, ROUND_HALF_UP

compra = Decimal(input("Ingrese el monto de compra: "))

print(f"El monto de la compra sin redondeo es {compra} soles.")

compra = compra.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print(f"El monto de la compra con redondeo es {compra} soles.")