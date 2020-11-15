from empleado import Empleado
from gerente import Gerente 


def imprimr_detalles(tipo_padre):
    print(tipo_padre);
    if(isinstance(tipo_padre,Gerente)):
        print(tipo_padre.departamento);
    print("\n");

empleado=Empleado("Juan",100.00);

imprimr_detalles(empleado);

empleado=Gerente("kKarla",2000.00,"Sistemas");
imprimr_detalles(empleado);