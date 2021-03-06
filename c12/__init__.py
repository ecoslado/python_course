__author__ = 'jesus.pedro.gutierrez.almazan'

var_one, var_two, var_three, var_four = None

# Alinear con el delimitador de apertura.
def long_function_name(var_one, var_two,
                       var_three, var_four):
    pass


# Hanging indents *may* be indented to other than 4 spaces.
foo = long_function_name(
  var_one, var_two,
  var_three, var_four)


# Añadir indentacion extra en una condición larga
# Si se tabula a 4 espacios, coincide con la siguiente
# linea del cuerpo y visualmente confunde
if (var_four
        and var_one):
    long_function_name(var_one, var_two, var_three, var_four)




# El separador, en contrucciones largas, se puede 
# colocar:
# Debajo del primer caracter no blanco de la ultima linea de la construccion
# Alineado con el primer caracter no blanco de la linea que inicia la contruccion

my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

my_list = [
    1, 2, 3,
    4, 5, 6,
]


# Usar espacios en vez de tabuladores
# Se recomienda utilizar 4 espacios extra en cada indentacion


# Limitar la longitud de linea a 79 caracteres


# Separar la definicion de funciones y clases por dos lineas blancas
# Separar los metodos por una linea blanca
# Se puede utilizar una linea blanca para separar secciones logicas de codigo


# Importaciones, una en cada linea
# Yes: 
import os
import sys
     
# No
import sys, os

# Es correcto hacer:
from subprocess import Popen, PIPE


# Absoluto mejor que relativo
"""
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
"""

# Evitar importar con wildcards



# Otros desastres a evitar
# Yes:

x = 1
y = 2
long_variable = 3

# No:

x             = 1
y             = 2
long_variable = 3

"""
b (single lowercase letter)

B (single uppercase letter)

lowercase

lower_case_with_underscores

UPPERCASE

UPPER_CASE_WITH_UNDERSCORES

CapitalizedWords (or CapWords, or CamelCase -- so named because of the bumpy look of its letters [3] ). This is also sometimes known as StudlyCaps.

Note: When using abbreviations in CapWords, capitalize all the letters of the abbreviation. Thus HTTPServerError is better than HttpServerError.

mixedCase (differs from CapitalizedWords by initial lowercase character!)
"""
