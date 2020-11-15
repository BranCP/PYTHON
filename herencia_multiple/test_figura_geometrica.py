from cuadrado import Cuadrado
from cuadrado import Rectangulo
from figura_geometrica import FiguraGeometrica


#no es posible crear objetos de una clase abstracta
#figuraGeometrica=FiguraGeometrica(4,5);

cuadrado=Cuadrado(4,"rojo");

print(cuadrado.area());
#print(cuadrado.area());

#method resolution order
print(Cuadrado.mro());

rectangulo=Rectangulo(4,3,"verde");
print(rectangulo);