__author__ = 'Enrique Coslado'

def main():
    try:
        provinces = dict()
        for name in ["Madrid", "Barcelona", "Sevilla", "Jaen"]:
            provinces[name] = dict(cities = list())

        cities_in_madrid = ["Buitrago de Lozoya", "Getafe", "Parla", "Cadalso de los Vidrios"]

        provinces["Madrid"] = cities_in_madrid

        print provinces["Teruel"]


    except KeyError as e:
        print "This province or city does not exist. %s" % repr(e)

    except IndexError as e:
        print "There's no city for that position. %s" % repr(e)

    except Exception as e:
        print "Woops. There was a problem. %s" % repr(e)

if __name__ == "__main__":
    main()