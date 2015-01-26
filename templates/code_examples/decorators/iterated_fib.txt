__author__ = 'Enrique Coslado'
import time

def fib(n):
    f = 1
    f1 = 1
    f2 = 1
    for i in range(n + 1):
        if i > 1:
            f = f1 + f2
            f2 = f1
            f1 = f

    return f


def main():
    init = time.clock()
    print fib(30)
    end = time.clock()
    delta = end - init
    print "Time spent: %s seconds." % delta

    init = time.clock()
    print fib(1000)
    end = time.clock()
    delta = end - init
    print "Time spent: %s seconds." % delta

if __name__ == "__main__":
    main()