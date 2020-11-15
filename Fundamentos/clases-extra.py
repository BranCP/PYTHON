class Persona:
    def __init__(this,n,e, *v,**d):
        this.nombre=n
        this.edad=e
        this.valores= v #*v se está insertando una tupla, el asterisco es de parametro opcional
        this.diccionario=d
        
        
    def desplegar(this):
        print("Nombre: ",this.nombre);
        print("Edad: ",this.edad);
        print("Valores (tupla): ",this.valores);
        print("Diccionario :", this.diccionario);
        
p1=Persona("juan",28);

print(p1.nombre);
print(p1.edad);

p1.desplegar();

p2= Persona("Karla",30,2,4,5);

p2.desplegar();

p3=Persona("Paola",33,4,9,m="manzana",p="pera",j="Jicama");
p3.desplegar();