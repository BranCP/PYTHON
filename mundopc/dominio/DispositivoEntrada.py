class DispositivoEntrada:
    def __init__(self,tipo_entrada,marca):
        self._tipo_entrada=tipo_entrada;
        self._marca=marca
    
    def get_tipo_entrada(self):
        return self._tipo_entrada
    
    def set_tipo_entrada(self,tipo_entrada):
        self._tipo_entrada=tipo_entrada;
        
    def get_marca(self):
        return self._marca;
    
    def set_marca(self,marca):
        self._marca=marca


class Raton(DispositivoEntrada):    
    contador_ratones=0;
    
    def __init__(self,entrada,marca):
        super().__init__(entrada,marca)
        Raton.contador_ratones+=1
        self.__id_raton=Raton.contador_ratones
    
    def __str__(self):
        return (
            f"Id: {self.__id_raton}, "
            f"Marca: {super().get_marca()}, "
            f"tipo entrada: {super().get_tipo_entrada()}"
        )
       # return "Ratón ID: " + str(self.__id_raton) + ", marca: " + super().get_marca() + ", tipo_entrada: " + super().get_tipo_entrada()
    
class Teclado(DispositivoEntrada):
    contador_teclados=0
    
    def __init__(self,entrada,marca):
        super().__init__(entrada,marca)
        Teclado.contador_teclados+=1
        self.__id_teclado=Teclado.contador_teclados
        
    def __str__(self):
        return "Teclado ID: " + str(self.__id_teclado) + ", marca: " + super().get_marca() + ", tipo_entrada: " + super().get_tipo_entrada()

class Monitor:
    contador_monitores=0
    
    def __init__(self,marca,tamanio):
        Monitor.contador_monitores+=1
        self.__id_monitor=Monitor.contador_monitores
        self.__marca=marca
        self.__tamanio=tamanio
    
    def __str__(self):
        return "Monitor: " + str(self.__id_monitor) + ", marca: " + self.__marca + ", tamaño: " + self.__tamanio
    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self,marca):
        self.__marca=marca
    
    def get_tamanio(self):
        return self.__tamanio
    
    def set_tamanio(self,tamanio):
        self.__tamanio=tamanio
        
class Computadora:
    contador_computadoras=0
    
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadoras+=1
        self.__id_computadora=Computadora.contador_computadoras
        self.__nombre=nombre
        self.__monitor=monitor
        self.__teclado=teclado
        self.__raton=raton
        
    def __str__(self):
        a=self.__nombre + ":" + str(self.__id_computadora) + "\n"
        a=a+self.__monitor.__str__() + "\n"
        a=a+self.__teclado.__str__() + "\n"
        a=a+self.__raton.__str__()
        
        return a;
        

class Orden:
    contador_ordenes=0;
    
    def __init__(self,computadora):
        Orden.contador_ordenes+=1
        self.__id_orden=Orden.contador_ordenes
        self.__computadora=computadora 
        
    def agregarComputadora(self,computadora):
        self.__computadora.append(computadora)
    
    def __str__(self):
        cadena=""
        for compu in self.__computadora:
            cadena+=compu.__str__() + "\n"        
        return (
            f"Orden: {self.__id_orden}, "
            f"Compuradoras: \n {cadena}"            
        )
    

raton=Raton("USB","HyperX");
raton2 = Raton("Wireless","Razer");

teclado1= Teclado("usb","razer")
teclado2= Teclado("wireless","hyperx")

monitor1=Monitor("Marca1","22")
monitor2=Monitor("Marca2","34")

computadora1=Computadora("HP",monitor1,teclado1,raton2);
computadora2=Computadora("Alienware",monitor2,teclado2,raton);

compus=[computadora1]
order_total=Orden(compus)
#print(order_total);
order_total.agregarComputadora(computadora2);
print(order_total);


# print(raton);
# print(raton2);

# print(teclado1)
# print(teclado2)

# print(monitor1)
# print(monitor2)