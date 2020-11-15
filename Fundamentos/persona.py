class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre #definiendo los atribuos, self hace refernecia al objeto
        self.edad=edad #cuales el parametro y cual es el atributo, self atributo
        
    #pass; # para que la pase, la clase vacia
#modificar valores
Persona.nombre="Juan";
Persona.edad=28;

#acceder a los valores
print(Persona.nombre);
print(Persona.edad);
#print(Persona); la clase en si misma es un objeto

#creacion de un objeto
persona = Persona("Papa",30);
prueba=Persona("aea");

print("edad de la prueba: ",prueba.edad);
