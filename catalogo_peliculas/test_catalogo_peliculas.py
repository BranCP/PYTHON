from dominio.pelicula import Pelicula
from servicio.catalogopelicula import CatalogoPeliculas

opcion=None;

while opcion!="4":
    print("Opciones:")
    print("1. Agregar pelicula")
    print("2. Listar películas")
    print("3. Eliminar catálogo de peliculas")
    print("4. Salir");
    opcion = input("Eliga opcion: ")
    
    if opcion=="1":
        nombre_peli = input("Ingrese nombre: ")
        nombre_peli += "\n"
        pelicula=Pelicula(nombre_peli)
        print(pelicula.get_nombre())
        CatalogoPeliculas.agregar_pelicula(pelicula);
    elif opcion=="2":
        CatalogoPeliculas.listar_peliculas();
    elif opcion=="3":
        CatalogoPeliculas.eliminar()
        
else:
    print("Salimos del programa");
