__author__ = 'Enrique Coslado'

import sys, os

try:
    provinces = dict()
    for name in ["Madrid", "Barcelona", "Sevilla", "Jaen"]:
        provinces[name] = dict(cities = list())

    cities_in_madrid = ["Buitrago de Lozoya", "Getafe", "Parla", "Cadalso de los Vidrios"]

    provinces["Madrid"] = cities_in_madrid

    print provinces["Teruel"]


except Exception as e:
    print "This province or city does not exist. %s" % repr(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)