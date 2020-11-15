from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado) #super llama a la del lado izquierdo
        Color.__init__(self,color)
        
    def area(self):
        return FiguraGeometrica.get_ancho(self)*FiguraGeometrica.get_ancho(self);
    
    def __str__(self):
        return  FiguraGeometrica.__str__(self) + ", " + Color.__str__(self);



class Rectangulo(FiguraGeometrica,Color):
    def __init__(self,ancho,alto,color):
        FiguraGeometrica.__init__(self,ancho,alto) #super llama a la del lado izquierdo
        Color.__init__(self,color)
        
    def area(self):
        return self.__alto*self.__ancho;
    
    def __str__(self):
        return  FiguraGeometrica.__str__(self) + ", " + Color.__str__(self);
