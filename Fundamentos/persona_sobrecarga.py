class Persona:
    def __init__(self,nombre):
        self.__nombre=nombre;
    
    #metodo sobreescrito de la clase padre object        
    def __add__(self,otro):
        return self.__nombre +  otro.__nombre;
    
    def __sub__(self,otro):
        return "operacion no soportada";
        
p1=Persona("Juan");
p2=Persona("Karla");

print(p1+p2); #esto llama al metdo + de la clase objet, podemos sobreescribirlo

print(p1-p2);