class Persona:
    def __init__(self,nombre,ape_paterno,ape_materno):
        self.nombre=nombre; #si no tiene "_" es publico, 1 _ es protegido, 2 __ es privado
        self._ape_paterno=ape_paterno; #no necesita get o set
        self.__ape_materno=ape_materno;
        
    def metodo_publico(self):
        self.__metodo_privado();
        
    def __metodo_privado(self): #metodo privado
        print(self.nombre)
        print(self._ape_paterno);
        print(self.__ape_materno);
        

p1=Persona("Juan","lopera","perez");
p1.metodo_publico();

print(p1.nombre);
print(p1._ape_paterno);

    
        