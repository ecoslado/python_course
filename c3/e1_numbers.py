__author__ = 'Enrique Coslado'

import decimal

def add_float_int(float_a, int_b):
    return float_a + int_b

def add_float_float(float_a, float_b):
    return float_a + float_b

def add_decimal_decimal(decimal_a, decimal_b):
    return decimal_a + decimal_b

def divide_int_int(int_a, int_b):
    return int_a / int_b

def _print_result(result):
    print "Result by default"
    print result
    print "28 decimal precision"
    print "{:.28f}".format(result)

def main():
    # Initializing numbers
    int_a = 4
    int_b = 5
    float_a = 1.1
    float_b = 4.0
    decimal_a = decimal.Decimal("1.1")
    decimal_b = decimal.Decimal("4.")

    # Basic operations with numbers
    print "Float %s + Integer %s" % (float_a, int_b)
    result = add_float_int(float_a, int_b)
    _print_result(result)

    print "Float %s + Float %s" % (float_a, float_b)
    result = add_float_float(float_a, float_b)
    _print_result(result)

    print "Decimal %s + Decimal %s" % (decimal_a, decimal_b)
    result = add_decimal_decimal(decimal_a, decimal_b)
    _print_result(result)

    print "Int %s / Int %s" % (int_a, int_b)
    result = divide_int_int(int_a, int_b)
    _print_result(result)


if __name__ == "__main__":
    main()

