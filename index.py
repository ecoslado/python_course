# -*- coding: utf-8 -*-
__author__ = 'Enrique Coslado'
from flask import url_for

index = [
    {
        "title": "Introduction",
        "items": [
            {
                "title": "Que es Python",
                "chapter": "introduccion",
                "example": "introduccion"
            }
        ]
    },
    {
        "title": "Starting Flask Server",
        "items": [
            {
                "title": "Iniciando el servidor Flask",
                "chapter": "servidor",
                "example": "arrancar"
            }
        ]
    },
    {
        "title": "Basic types in Python",
        "items": [
            {
                "title": "Numbers",
                "chapter": "basic_types",
                "example": "numbers"
            },
             {
                "title": "Strings",
                "chapter": "basic_types",
                "example": "strings"
            },
             {
                "title": "Lists and dicts",
                "chapter": "basic_types",
                "example": "list_and_dict"
            },
             {
                "title": "Mutable vs. Immutable",
                "chapter": "basic_types",
                "example": "mutable_immutable"
            },
        ]
    },
    {
        "title": "Flow Managing",
        "items": [
            {
                "title": "Sentencia if",
                "chapter": "flujo",
                "example": "if"
            },
            {
                "title": "Sentencia for",
                "chapter": "flujo",
                "example": "for"
            },
            {
                "title": "Sentencia while",
                "chapter": "flujo",
                "example": "while"
            },
            {
                "title": "Funcion range",
                "chapter": "flujo",
                "example": "range"
            },
            {
                "title": "Otras sentencias",
                "chapter": "flujo",
                "example": "others"
            },
            {
                "title": "'Comprension' de listas",
                "chapter": "flujo",
                "example": "comprehension"
             },
            {
                "title": "Generadores",
                "chapter": "flujo",
                "example": "generators"
            }
        ]
    },
    {
        "title": "Application Structure",
        "items": [
            {
                "title": "Scopes",
                "chapter": "application_structure",
                "example": "scopes"
            },
            {
                "title": "Local and Global",
                "chapter": "application_structure",
                "example": "local_and_global"
            },
            {
                "title": "LEGB (Local, enclosed, global, builtin hierarchy)",
                "chapter": "application_structure",
                "example": "LEGB"
            },
            {
                "title": "For loop gotcha",
                "chapter": "application_structure",
                "example": "for_loop"
            },
            {
                "title": "Mutable arguments",
                "chapter": "application_structure",
                "example": "mutable_args"
            },

        ]
    },
    {
        "title": "Object Oriented Programming",
        "items": [
            {
                "title": "Clases en Python",
                "chapter": "object_oriented",
                "example": "clases"
            },
            {
                "title": "Herencia",
                "chapter": "object_oriented",
                "example": "herencia"
            },
            {
                "title": "Basic Abstract Class",
                "chapter": "object_oriented",
                "example": "products"
            },
            {
                "title": "ABC Inherited Abstract Class",
                "chapter": "object_oriented",
                "example": "products2"
            },
            {
                "title": "Inheriting Abstract Classes",
                "chapter": "object_oriented",
                "example": "special_products"
            },
            {
                "title": "Atributos privados y muy privados",
                "chapter": "object_oriented",
                "example": "privated"
            },
            {
                "title": "Ejercicio",
                "chapter": "object_oriented",
                "example": "ejercicio"
            }
        ]
    },
    {
        "title": "Exceptions Managing",
        "items": [
            {
                "title": "Simple Try Except",
                "chapter": "exceptions",
                "example": "simple_try_except"
            },
            {
                "title": "Catching different exception types",
                "chapter": "exceptions",
                "example": "catching_some_types"
            },
            {
                "title": "Exception Execution Frame",
                "chapter": "exceptions",
                "example": "execution_frame"
            },

        ]
    },
    {
        "title": "Some String Services",
        "items": [
            {
                "title": "Servicios de cadenas",
                "chapter": "string_services",
                "example": "re"
            },

        ]
    },
    {
        "title": "Managing date and time",
        "items": [
            {
                "title": "Time package",
                "chapter": "managing_time",
                "example": "time"
            },
            {
                "title": "Datetime package",
                "chapter": "managing_time",
                "example": "datetime"
            },
            {
                "title": "Calendar package",
                "chapter": "managing_time",
                "example": "calendar"
            },
        ]
    },
    {
        "title": "Decorators",
        "items": [
            {
                "title": "Recursive Fibonacci",
                "chapter": "decorators",
                "example": "recursive_fib"
            },
            {
                "title": "Caching Recursive Fibonacci",
                "chapter": "decorators",
                "example": "caching_recursive_fib"
            },
            {
                "title": "Simply decorated Fibonacci",
                "chapter": "decorators",
                "example": "simple_decorated_caching"
            },
            {
                "title": "Separated Cached Decorator",
                "chapter": "decorators",
                "example": "separated_cached_decorator"
            },
            {
                "title": "Separated Fibonacci",
                "chapter": "decorators",
                "example": "separated_fib"
            },
            {
                "title": "Iterative Fibonacci",
                "chapter": "decorators",
                "example": "iterated_fib"
            },
        ]
    },
    {
        "title": "Map and Reduce",
        "items": [
            {
                "title": "Map",
                "chapter": "mapreduce",
                "example": "mapreduce"
            }
        ]
    },
    {
        "title": "Buenas practicas",
        "items": [
            {
                "title": "Buenas practicas",
                "chapter": "guia_estilo",
                "example": "pep8"
            }
        ]
    },
    {
        "title": "Recursos remotos",
        "items": [
            {
                "title": "HTTP",
                "chapter": "recursos_red",
                "example": "acceso_http"
            },
            {
                "title": "FTP",
                "chapter": "recursos_red",
                "example": "acceso_ftp"
            }
        ]
    }
]


