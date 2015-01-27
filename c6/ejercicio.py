__author__ = 'jesus.pedro.gutierrez.almazan'
import StringIO

def ejercicio():
    class Lee_lineas(object):
        def abrir(self, obj):
            raise NotImplementedError("Not implemented")
    
        def lee_linea(self):
            raise NotImplementedError("Not implemented")
            
        def cerrar(self):
            raise NotImplementedError("Not implemented")
    
    class Lee_fichero(Lee_lineas):
        _fd = None
        
        def abrir(self, obj):
            self._fd = open(obj, 'r')
        
        def lee_linea(self):
            if self._fd:
                linea = self._fd.readline()
                while linea:
                    yield linea
                    linea = self._fd.readline()
    
        def cerrar(self):
            self._fd.close()
            
    class Lee_string(Lee_lineas):
        _string_io = None
        
        def abrir(self, obj):
            self._string_io = StringIO.StringIO(obj)
    
        def lee_linea(self):
            if self._string_io:
                linea = self._string_io.readline()
                while linea:
                    yield linea
                    linea = self._string_io.readline()
    
        def cerrar(self):
            self._string_io.close()
    
    lector = Lee_fichero()
    lector.abrir('servidor.py')
    for line in lector.lee_linea():
        print line
    
    lector.cerrar()
    
    lector = Lee_string()
    lector.abrir("""
    linea1
    linea2
    linea3
    """)
    for line in lector.lee_linea():
        print line
    
    print type(lector)
    
    print isinstance(lector, Lee_fichero)
    
    print isinstance(lector, Lee_lineas)
    
    print issubclass(Lee_fichero, Lee_string)
    
    
    lector.cerrar()

def main():
    ejercicio()

if __name__ == "__main__":
    main()