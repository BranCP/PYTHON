condicion = True;

print("Condicion verdadera") if condicion else print("condicion falsa");

if condicion==True:
    print("verdadero")
elif condicion==False:
    print("la condicion es falsa")
else:
    print("wtf")
    

numero =int(input("Ingrese el numero: "))

if numero==1:
    numeroTexto ="Numero uno"
elif numero ==2:
    numeroTexto="numero dos"
elif numero ==3:
    numeroTexto="numero tres"
else:
    numeroTexto = "Valor fuera de rango"
    
print("numero es: ",numeroTexto);