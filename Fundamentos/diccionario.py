#un diccionario está compuesto de llave, valor key,value

diccionario={
    "IDE": "integrated develpomnent environment",
    "OOP":"Object Oriented Programming",
    "DBMS": "Database Management System"
}

print(diccionario);
#largo
print(len(diccionario));
#accediento a un elemento
print(diccionario["IDE"]);
#otra forma, mismo resultado
print(diccionario.get("IDE"));
#modificando valores
diccionario["IDE"]='Hola';
print(diccionario["IDE"]);
#iterar
for termino in diccionario:
    print(termino);

for termino in diccionario:
    print(diccionario[termino]);
    
for valor in diccionario.values():
    print(valor);
    
#comprobando inxistencia en un elemento"
print("IDE" in diccionario);

#agregar nuevos elementos
diccionario["PK"]='Primary Key';
print(diccionario["PK"]);

#remover elementos
diccionario.pop("DBMS");
print(diccionario);

#limpiar
diccionario.clear();

#eliminar 
del diccionario