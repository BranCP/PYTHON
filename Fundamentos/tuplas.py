#tupla mantiene el orden pero no se puede modificar
frutas = ('manzana','pera');

print(frutas);

#largo de la tupla
print(len(frutas));
print(frutas[0]);
#navegacion inversa
print(frutas[-1]);
#rango 
print(frutas[:]); #excluyendo el indice 2
#modificar un valor
#frutas[0]="asdasd";
frutaLista=list(frutas);

frutaLista.append('fruta new');
frutas=tuple(frutaLista);
print(frutas);
print(type(frutas));

#iterar una tupla
for fruta in frutas:
    print(fruta,end="||");
    
#nopodemos agregar ni eliminar elementos de una tupla
del frutas


tupla = (13,1,8,3,2,5,8);
lista=[];

for tup in tupla:
    if(tup<5):
        lista.append(tup);
        
print(lista);