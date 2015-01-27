__author__ = 'jesus.pedro.gutierrez.almazan'

def e1_clases():
    # Una clase vacia (como registro de C)
    class A(object):
        """
        Documentacion clase A
        """
        pass
    
    print A.__doc__
    
    # Una clase con un atributo
    class B(object):
        """
        Documentacion clase A
        """
        attr = 'Soy un atributo'
    print B.attr
    
    # Setear atributos
    class C(object):
        attr = 'kkkk'
    
    print C.attr
    
    C.nombre = 'paco'
    C.attr = 'otro valor'
    print A.attr
    print A.nombre
    
    
    # Constructor
    class D(object):
        def __init__(self, nombre, alias):
            self.nombre = nombre
            self.alias = alias
    
    mi_clase = D('antonio', 'machine')
    print mi_clase.nombre
    print mi_clase.alias
    
    # La clase D no tiene atributo nombre
    print D.nombre
    
    # Objetos de instancia
    class MiClase(object):
        i = 10
        def mi_metodo(self):
            print 'Soy un metodo feliz'
            
    miclase = MiClase()
    
    # Cuando se trata de una clase, MiClase.mi_metodo es una funcion.
    # Cuando se trata de una instancia, miclase.mi_metodo es un metodo.
    
    # Metodo y funcion son diferentes, el primero es atributo de clase
    # mientras que el segundo es un atributo de objeto
    
    
    # Objetos Metodo
    variable = miclase.mi_metodo
    while True:
        variable()
        
    # El anterior codigo pintara la cadena "Soy un metodo feliz" hasta el infinito
    # ATRIBUTOS DE DATOS ----> Tienen preferencia sobre atributos de metodos con igual nombre!!
    
    
    # Metodos y atributos se pueden llamar con self
    class Bolsa:
        def __init__(self):
            self.datos = []
        def agregar(self, x):
            self.datos.append(x)
        def dobleagregar(self, x):
            self.agregar(x)
            self.agregar(x)

def main():
    e1_clases()

if __name__ == "__main__":
    main()
