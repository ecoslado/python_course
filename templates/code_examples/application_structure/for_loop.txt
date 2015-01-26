__author__ = 'Enrique Coslado'

a = 2
for a in range(5):
    if a == 4:
        print(a, '-> a in for-loop')
print(a, '-> a in global')


i = 1
print([i for i in range(5)])

# This behaviour changes in Python 3.x
print(i, '-> i in global')