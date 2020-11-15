class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre;
        self.edad=edad;
        
    def __str__(self):
        return "Nombre: " + self.nombre + ", edad: " + str(self.edad);
        
        
class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad);
        self.sueldo=sueldo;
    
    def __str__(self):
        return super(Empleado,self).__str__() + ", sueldo: " + str(self.sueldo); 
        
        
persona=Persona("Pedro",28);
print(persona);

empleado=Empleado("Pedro",27,1400.00);
print(empleado);


class Vehiculo:
    def __init__(self,color,ruedas):
        self.color=color;
        self.ruedas=ruedas;
    
    def __str__(self):
        return "Vehiculo color: " + self.color + " con ruedas: " + str(self.ruedas)


class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas);
        self.velocidad=velocidad;
        
    def __str__(self):
        return super().__str__() + ", velocidad de : " + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas);
        self.tipo=tipo;
        
    def __str__(self):
        return super().__str__() + ", del tipo : " + self.tipo;
    

vehiculo=Vehiculo("rojo",4);
print(vehiculo);

coche=Coche("verde",3,40);
print(coche);

bicicleta=Bicicleta("negro",8,"urbana");
print(bicicleta);