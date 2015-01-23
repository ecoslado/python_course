__author__ = 'kike'
import copy
from decimal import Decimal

def variable_info(any_var):
    return "%s variable with value %s is in address %s." % (type(any_var), any_var, id(any_var))

def main():
    a = 5
    print variable_info(a)
    a += 2
    print "Added 2 to integer a"
    print variable_info(a)

    b = "Hello"
    print variable_info(b)
    print "Appending world to string."
    b += " world"
    print variable_info(b)

    c = list()
    print variable_info(c)
    print "Appending integer to the list."
    c.append(a)
    print variable_info(c)

    c = Decimal("4.")
    d = Decimal("5.")
    print variable_info(c)
    print "Adding 4. to decimal variable."
    c += d
    print variable_info(c)

    c = dict()
    print variable_info(c)
    print "Assigning bar to key foo."
    c["foo"] = "bar"
    print variable_info(c)


    print "Simple copy of a dictionary."
    print variable_info(c)
    d = c
    print variable_info(d)

    print "Deep copy of a dictionary."
    print variable_info(c)
    d = copy.deepcopy(c)
    print variable_info(d)

if __name__ == "__main__":
    main()