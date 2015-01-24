__author__ = 'jesus.pedro.gutierrez.almazan'
import inspect

def get_source_lines(func):
    return inspect.getsourcelines(func)[0]