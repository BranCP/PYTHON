



a="10"
b=0 
resultado=None

try:
    resultado=a/b
#except ZeroDivisionError as e: primero va la de menor jerarquia
except ZeroDivisionError as e:
    print("Ocurrio un error zero",e);
    print(type(e));
except TypeError as e:
    print("Ocurrio un error type",e);
    print(type(e));
except Exception as e:
    print("Ocurrio un error excep",e);
    print(type(e));
#si ponemos la exceptin de mayor jerarquia arriba, solo ejecutará hasta este punto



print("resultado: ",resultado);



try:
    10/0
except Exception as e:
    
    print("Ocurrio un error: ",e);
    
print("continuamos: ");