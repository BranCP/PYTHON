class Aritmetica:
    def __init__(self,operando1,operando2):
        self.operando1=operando1;
        self.operando2=operando2;
        
    def sumar(self): #todos los metodos dentro de una clase necesitan el metodo self
        """ se realiza la operacion con atributos de la clase """
        return self.operando1 + self.operando2;
    
#creamos un nuevo objeto

aritmetica= Aritmetica(3,4);

print("La suma es: ",aritmetica.sumar());

class Rectangulo:
    def __init__(self,base,altura):
        self.base=base;
        self.altura=altura;
        
    def calcularArea(self):
        return self.base*self.altura;

base=int(input("Ingrese la base: "));
altura=int(input("Ingrese la altura: "));

rectangulo1 = Rectangulo(base,altura);

print("El área es : ",rectangulo1.calcularArea());

class Caja:
    def __init__(self,base,altura,largo):
        self.base=base;
        self.altura=altura;
        self.largo=largo;
        
    def calcularVolumen(self):
        return self.base*self.altura*self.largo;

base1=int(input("Ingrese la base: "));
altura1=int(input("Ingrese la altura: "));
largo1=int(input("Ingrese el largo:"));

caja1 = Caja(base1,altura1,largo1);

print("El volumen es : ",caja1.calcularVolumen());
