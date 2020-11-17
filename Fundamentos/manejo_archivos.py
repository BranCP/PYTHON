try:
    archivo=open("prueba.txt","w");
    archivo.write("agregando info al archivo\n");
    archivo.write("adios");
except Exception as e:
    print(e);
finally:
    archivo.close();
    
#despues de close ya no podemos trabajar con el archivo
#archivo.write("saludos")