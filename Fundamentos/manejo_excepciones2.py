from numeros_identificos_exception import NumeroIdenticosException
resultado = None

try:
    a=int(input("Primer número: "));
    b=int(input("Segundo número: "))
    if a==b:
        raise NumeroIdenticosException("Ocurrio un error,numerosiguales"); #lanzar en ingles
    resultado= a/b
except ZeroDivisionError as e:
    print("Ocurrio un error zero",e);
    print(type(e));
except TypeError as e:
    print("Ocurrio un error type",e);
    print(type(e));
except ValueError as e:
    print("Valiu error");
    print(type(e));
except Exception as e:
    print("Ocurrio un error excep",e);
    print(type(e));
else:
    print("no hubo excepcion") #el else es cuando no tenemos ningun error y queremos lanzar un mensaje, bloque opcional
finally:
    print("Este bloque siempre se ejecuta") #siempre se ejecuta solo por el echo de entrar al bloque try
    
