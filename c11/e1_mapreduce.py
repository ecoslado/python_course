
def e1_mapreduce():
    # MAP
    # map(aFunction, aSecuence, [aSecuence, ...])
    #
    # Queremos realizar una operacion sobre una lista de elementos
    items = [1, 2, 3, 4, 5]
    squared = []
    for x in items:
        squared.append(x ** 2)
    
    print squared
    
    
    # La funcion map realiza esta tarea de una manera simplificada
    items = [1, 2, 3, 4, 5]
    def sqr(x): return x ** 2
    print list(map(sqr, items))
    
    # La funcion sqr anterior se sustituir por una funcion anonima (funcion lambda)
    print list(map((lambda x: x ** 2), items))
    
    
    # Map puede recoger un numero arbitrario de parametros
    # Creara pares entre elementos pertencientes a los parametros y aplicara una funcion sobre dichos pares
    # Si no se indica una funcion, devuelve la tupla creada.
    m = [1, 2, 3]
    n = [1, 4, 9]
    print map(None, m, n)
    
    
    # FILTER
    # filter(aFunction or None, aSecuence)
    #
    # La funcion filter extrae elementos de una secuencia y 
    # devuelve aquellos que devuelvan Verdadero al aplicar una funcion sobre ellos
    a = [1, 2, None, 4, 5, None, 7, 8, None]
    print filter(None, a)
    
    # REDUCE
    # reduce(aFunction, aSecuence[, initial])
    #
    # La funcion reduce aplica una funcion sobre pares de elementos de una secuencia hasta dejar un solo valor.
    print reduce((lambda x, y: x * y), [1, 2, 3, 4])
    
def main():
    e1_mapreduce()
    
if __name__ == "__main__":
    main()
