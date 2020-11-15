class Persona:
    def __init__(self,n,e):
        self.__nombre=n;
        self.__edad=e;
        
    def get_nombre(self):
        return self.__nombre;
    
    def set_nombre(self,nombre):
        self.__nombre=nombre;
        
    def get_edad(self):
        return self.__edad;
    
    def set_edad(self,edad):
        self.__edad=edad;
        
p1=Persona("Juan");
print(p1.get_nombre());
print(p1.get_edad());
p1.set_nombre("Brany");
p1.set_edad(17);
print(p1.get_nombre());
print(p1.get_edad());

# p1.__nombre="Hola";
# print(p1.nombre);