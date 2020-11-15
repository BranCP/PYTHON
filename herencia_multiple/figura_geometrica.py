#ABC = Abstract Base Class
from abc import ABC, abstractmethod



class FiguraGeometrica(ABC): #SU CLASE PADRE ES ABC
    def __init__(self,ancho,alto):
        self.__ancho=ancho;
        self.__alto=alto;
   
    def set_ancho(self,ancho):
        self.__ancho=ancho;
        
    def get_ancho(self):
        return self.__ancho;
    
    def set_alto(self,alto):
        self.__alto=alto;
    
    def get_alto(self):
        return self.__alto;
    
    def __str__(self):
        return "Figura Geometrica lado: " + str(self.__alto) + ", ancho: " + str(self.__ancho);
    
    @abstractmethod
    def area(self):
        pass #para pasar
    #metodo abstracto no tiene la implementación, si una clase 
    # tiene metodo abstracto, la clase s vuelve abstracta y 
    # no puede crearse objetos de esta clase
    
    
    
    
 

# class FiguraGeometrica():
#     def __init__(self,ancho,alto):
#         self.__ancho=ancho;
#         self.__alto=alto;
   
#     def set_ancho(self,ancho):
#         self.__ancho=ancho;
        
#     def get_ancho(self):
#         return self.__ancho;
    
#     def set_alto(self,alto):
#         self.__alto=alto;
    
#     def get_alto(self):
#         return self.__alto;
    
#     def __str__(self):
#         return "Figura Geometrica lado: " + str(self.__alto) + ", ancho: " + str(self.__ancho);
    
#     #metodo abstracto no tiene la implementación, si una clase 
#     # tiene metodo abstracto, la clase s vuelve abstracta y 
#     # no puede crearse objetos de esta clase
       
    