#set es una coleccion sin orden y sin indices, no permite elementos repetidos
#y los elementos no se pueden modificar, si agregar nuevos o eliminar

planetas= {"Tierra","Marte","Jupiter"}
print(planetas)

#largo
print(len(planetas));
#revisar si un element oesta presente
print("Marte" in planetas);
#agregar
planetas.add("tierra");
print(planetas)
#eliminar
planetas.remove("Tierra");
print(planetas);
#eliminar con discard no arroja excepcion
planetas.discard("Jupiter");
print(planetas);
#limpiar el set
planetas.clear();
print(planetas);
#eliminar el set
del planetas;
print(planetas);