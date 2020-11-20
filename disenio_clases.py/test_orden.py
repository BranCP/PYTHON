from producto import Producto
from orden import Orden

producto1=Producto("Camisa",100);
producto2=Producto("Pantalon",200);
producto3=Producto("Calcetines",50.00);

#lista
productos=[producto1,producto2];
print(type(productos))

orden1=Orden(productos);

print(orden1);

productos.append(producto3);
orden2=Orden(productos);
print(orden2);
print(orden2.calcular_total());
producto4=Producto("Prueba",10.0);
orden2.agregar_producto(producto4);
print(orden2);
print(orden2.calcular_total());