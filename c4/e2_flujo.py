__author__ = 'jesus.pedro.gutierrez.almazan'

def flow_control_comprehension():
    numbers = range(10)
    print numbers
    numbers = [number for number in numbers if number < 5]
    print numbers

    numers_dict = {str(i):i for i in range(10) if i > 5}
    print numers_dict
    
def flow_control_others():
    if True:
        pass
    
    for i in range(10):
        if i == 5:
            continue
        print i
    print i

    for i in range(10):
        if i == 5:
            break
        print i
    print i
    
    for i in range(10):
        if i == 5:
            continue
        print i
    else:
        print 'colorin colorado'

    for i in range(10):
        if i == 5:
            break
        print i
    else:
        print 'colorin colorado'
        
    def args_empty():
        pass
    args_empty()
    
    def args_param(param1):
        print param1
    args_param('hola')
    
    def args_named(name='John', movie='Rambo II'):
        print name
        print movie
    args_named(name='Silvester', movie='Cobra')
    
    def args_multiparam(*args):
        print args
    args_multiparam('param1', 'param2', 'param3')
    
    def args_namedparam(**kwargs):
        print kwargs
    args_namedparam(name='John', alias='Rambo')
    
    def args_mixedparams(*args, **kwargs):
        print args
        print kwargs
    args_mixedparams('usuario', 'pagina', name='John', alias='Rambo')
    
    def args_mixedparams_2(categoria, *args, **kwargs):
        print categoria
        print args
        print kwargs
    args_mixedparams_2('cine', 'hoycinema', '/rambo2.html', name='John', alias='Rambo', actor='Silvester Stallone')

def flow_control_generators():
    # Generador de numeros
    def firstn(n):
        num, nums = 0, list()
        while num < n:
            nums.append(num)
            num += 1
        return nums

    print firstn(100)
    print sum(firstn(100))
    
    # Generador de numeros como un iterable
    class firstn_as_class(object):
        def __init__(self, n):
            self.n = n
            self.num = 0
        
        def __iter__(self):
            return self
        
        # Python 3 compatibility
        def __next__(self):
            return self.next()
        
        def next(self):
            if self.num < self.n:
                cur, self.num = self.num, self.num + 1
                return cur
            else:
                raise StopIteration()

    print firstn_as_class(100)
    print sum(firstn_as_class(100))
            
    # Generador de numeros como un generador
    def firstn_as_generator(n):
        num = 0
        while num < n:
            yield num
            num += 1
    print firstn_as_generator(100)
    print sum(firstn_as_generator(100))
    
    # Generador de numeros como un 'generator comprehension'
    firstn_generator_comprehension = (i for i in xrange(100))
    print firstn_generator_comprehension
    print sum(firstn_generator_comprehension)
    
    
def main():
    flow_control_comprehension()
    flow_control_others()
    flow_control_generators()

if __name__ == "__main__":
    main()
