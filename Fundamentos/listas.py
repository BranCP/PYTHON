nombre = ['hola',2,'3'];

print(nombre[0]);

print(len(nombre));

print(nombre[-1]);

print(nombre[0:2]); #sin incluir el indice 2
#imprimir los elementos de inicio hasta el indice  proporcionado
print(nombre[:2]); #sin incluir el indice 2
print(nombre[1:]);


nombre.append("nuevo");
print(nombre);
nombre[3]="holaaaa";
print(nombre);

for name in nombre:
    print(name);
    
if "Karla" in nombre:
    print("existe"); 
else:
    print("no existe");   
    
#agregar un nuevo elemento
nombre.append("new");
print(nombre);

#insertar un nuevo elemento en el indice proporcionado
nombre.insert(1,"octavio");
print(nombre);
#remover un elemento 
nombre.remove("octavio");
#remover el ultimo elemento de lista
nombre.pop();
print(nombre);
#remover el indice indicado de la lista
del nombre[0];
print(nombre);
#limpiar los elementos denuestra lista
nombre.clear();

#eliminar por completo la lista
del nombre;

numeros=[]
i=0
while (i<=10):
    numeros.append(i);
    i+=1;
    
for numero in numeros:
    if numero%3==0:
        print("numero es: ",numero);
        
