__author__ = 'Enrique Coslado'

i = 1

def foo():
    i = 5
    print(i, 'in foo()')

foo()

print(i, 'global')

