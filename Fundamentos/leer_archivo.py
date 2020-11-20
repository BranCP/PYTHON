

try:
    archivo=open("D:\\Cursos\\PYTHON\\PYTHON\\prueba.txt","r");
    #print(archivo.read()); #lee todo el archivo, si viene otro print, no hay nada que leer
    #leer algunos caracteres
    # print(archivo.read(5));
    # print(archivo.read(3));
    # #leer lineas completas
    # print(archivo.readline());
    # print(archivo.readline())
    # #itererando
    # for linea in archivo:
    #     print(linea)
    #leer lineas
   # print(archivo.readlines())
   #acceder a una linea de la lista
    #print(archivo.readlines()[1])
    #abrimos un nuevo archivo
    archivo2=open("copia.txt","a");
    archivo2.write(archivo.read())
finally:
    archivo.close()
    archivo2.close()