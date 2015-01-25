__author__ = 'Enrique Coslado'
import time
from c10.e4_cached import cached

cache = dict()

def fib(n):
    return 1 if n < 2 else fib(n-1) + fib(n-2)
fib = cached(cache)(fib)

def main():
    init = time.clock()
    print fib(30)
    end = time.clock()
    delta = end - init
    print "Time spent: %s seconds." % delta

    init = time.clock()
    print fib(100)
    end = time.clock()
    delta = end - init
    print "Time spent: %s seconds." % delta

if __name__ == "__main__":
    main()