
import os
class CatalogoPeliculas:
    
    ruta_archivo="D:\\Cursos\\PYTHON\\PYTHON\\peliculas.txt"
    
    @staticmethod #variable estatitca no recibe ni self ni ctl
    def agregar_pelicula(pelicula):
        try:
            # a - modo append
            archivo=open(CatalogoPeliculas.ruta_archivo,"a")
            archivo.write(pelicula.__str__())
        except Exception as e:
            print("Ocurrio una excepcion al agregar: ",e)
        finally:
            archivo.close()
            
    @staticmethod
    def listar_peliculas():
        try:
            archivo=open(CatalogoPeliculas.ruta_archivo,"r")
            print("Catalogo de pelis: ")
            print(archivo.read()) 
        except Exception as e:
            print("Ocurrio un error al listar peliculas: ",e)
        finally:
            archivo.close()          
    
    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo);
            print("Archivo eliminado: ",CatalogoPeliculas.ruta_archivo);
        except Exception as e:
             print("Ocurrio un error al listar peliculas: ",e)
        

CatalogoPeliculas.listar_peliculas();
    