__author__ = 'jesus.pedro.gutierrez.almazan'
import inspect

def get_file_contents(filename):
    fd = open(filename, 'r')
    lines = fd.readlines()
    fd.close()
    return lines

def get_source_lines(obj):
    """
    Obtiene las lineas de codigo de un objeto, ya sea una funcion, modulo, frame, ...
    @param obj: Objeto del que obtener las lineas de codigo
    @return: Una lista de cadenas que son las lineas de codigo del objeto
    """
    return inspect.getsourcelines(obj)[0]