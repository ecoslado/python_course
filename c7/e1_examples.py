__author__ = 'Enrique Coslado'

try:
    provinces = dict()
    for name in ["Madrid", "Barcelona", "Sevilla", "Jaen"]:
        provinces[name] = dict(cities = list())

    cities_in_madrid = ["Buitrago de Lozoya", "Getafe", "Parla", "Cadalso de los Vidrios"]

    provinces["Madrid"] = cities_in_madrid

    print provinces["Teruel"]


except:
    print "This province or city does not exist."



