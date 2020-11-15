mes = int(input("Proporciona el mes del año (1-12): "))
estacion = None

if mes==1 or mes ==2 or mes==12:
    estacion="Invierno"
elif mes==3:
    estacion="Primavera"

print("Estacion: ",estacion," para el mes: ",mes)