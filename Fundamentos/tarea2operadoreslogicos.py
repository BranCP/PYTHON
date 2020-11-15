alto=int(input("Proporciona el alto: "));
ancho=int(input("Proporciona el ancho: "));

area=alto*ancho;
perimetro=(alto+ancho)*2;

print("Area: ",area);
print("Perímetro: ",perimetro);


num1=int(input("Proporciona el numero1: "));
num2=int(input("Proporciona el numero2: "));
numeroMayor=num1;

if (num1>num2):
    numeroMayor=num1;
else:
    if(num1==num2):
        numeroMayor=num1;
    else:
        numeroMayor=num2;
        
print("El número mayor es: ",numeroMayor);