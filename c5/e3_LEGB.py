__author__ = 'Enrique Coslado'

# Local -> Enclosed -> Global -> Built-in

# Local can be inside a function or class method, for example.
# Enclosed can be its enclosing function, e.g., if a function is wrapped inside another function.
# Global refers to the uppermost level of the executing script itself, and
# Built-in are special names that Python reserves for itself.

import numpy
import math
import scipy



print(math.pi, 'from the math module')
print(numpy.pi, 'from the numpy package')
print(scipy.pi, 'from the scipy package')

# LG
#a_var = 'global variable'
#def a_func():
#    print(a_var, '[ a_var inside a_func() ]')

#a_func()
#print(a_var, '[ a_var outside a_func() ]')

# LEG
#a_var = 'global value'

#def outer():
#    a_var = 'enclosed value'

#    def inner():
#        a_var = 'local value'
#        print(a_var)

#    inner()
#outer()

#a_var = 'global value'

#def outer():
#       global a_var
#       a_var = 'local value'
#       print('outer before:', a_var)
#       def inner():
#           global a_var
#           a_var = 'inner value'
#           print('in inner():', a_var)
#       inner()
#       print("outer after:", a_var)
#outer()

#a_var = 'global variable'

# LEGB
#def len(in_var):
#    print('called my len() function')
#    l = 0
#    for i in in_var:
#        l += 1
#    return l

#def a_func(in_var):
#    len_in_var = len(in_var)
#    print('Input variable is of length', len_in_var)

#a_func('Hello, World!')
