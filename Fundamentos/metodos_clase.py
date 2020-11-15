class MiClase:
    
    variable_clase="variable clase"
    
    def __init__(self):
        self.variable_instancia="Variable instancia"
    
    @staticmethod #no recibimos ningun parametro pero no accedemos al contexto de la clase
    def metodo_estatico():
        print("Metodo estatico papá");
        print(MiClase.variable_clase);   #para llamar a miclase, no tenemos variable self porque no hay objetos
        #print(MiClase.variable_instancia); # solo funciona cuando se crea un objeto
    
        
    @classmethod #recibe la variable cls 
    def metodo_clase(cls): #este metodo revise un parametro, self metodo de instancia, cls para metodos de clase
        print("Metodo de clase:" + str(cls));
        print(cls.variable_clase);
        #print(cls.variable_instancia); # solo funciona cuando se crea un objeto
    
    def metodo_instancia(self):
        self.metodo_estatico();
        self.metodo_clase();
        print(self.variable_clase);
        print(self.variable_instancia);
        

# MiClase.metodo_estatico();
# MiClase.metodo_clase();
objeto1=MiClase();
# objeto1.metodo_instancia();

objeto1.metodo_instancia();

#el contexto estatico no accede al dinamico, el dinamico si accede al estatico