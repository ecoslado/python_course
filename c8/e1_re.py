__author__ = 'jesus.pedro.gutierrez.almazan'
import re

def e1_re():
    if (re.search("b", "abc")):
        print "b esta en abc"
    
    # Un patron mas complicado
    if (re.search("\Aa[0-9].*(end|fin)$", "a7fin")):
        print "se ha encontrado el patron"
    
    # Rizando el rizo
    if (re.search("\Aa[0-9].*(end|fin)$", "a2 lo que quiera fin")):
        print "se ha encontrado el patron"
    
    
    # Las expresiones son case sensitive, se puede pasar flags
    # para modificar el comportamiento
    pattern = re.compile('H', re.IGNORECASE)
    result = pattern.search('aloha')
    
    # Como el resultado no es None, existe coincidencia
    print result == None
    
    
    
    # Tambien podemos partir cadenas con expresiones regulares
    pattern = re.compile('a[bc]')
    text = 'e8acjhf90abcklhd78ac867acaba8'
    pattern.split(text)
    
    
    
    # Agrupacion de coincidencias
    pattern = re.compile('(?P<name>.+)\.(?P<extension>.+)')
    result = pattern.match('hello.txt')
    result.group('name')
    
    result.group('extension')

def main():
    e1_re()

if __name__ == "__main__":
    main()