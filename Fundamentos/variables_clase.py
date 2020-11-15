class MiClase:
    
    variable_clase="Variable de Clase";
    
    def __init__(self,variable_instancia):
        self.variable_instancia=variable_instancia;
    
objeto1=MiClase("VariableIns");
print(MiClase.variable_clase);
print(objeto1.variable_instancia);

#podemos acceder a las variables de clase desde los objetos
print(objeto1.variable_clase);

#podemos acceder a las variables con el nombre de la clase
print(MiClase.variable_clase);


objeto1.variable_clase="Modificando variable de clase";

print(objeto1.variable_clase);
print(MiClase.variable_clase);

objeto2=MiClase("nuevo valor");

print(objeto2.variable_clase);

objeto3=MiClase("Tercer objeto");
MiClase.variable_clase="Cambio desde la clase" #esto lo ven los nw objetos

print(objeto1.variable_clase);
print(objeto2.variable_clase);
print(objeto3.variable_clase);