__author__ = 'kike'
import time

cache = dict()

def fib(n):
    if n not in cache:
        if n < 2:
            cache[n] = 1
        else:
            cache[n] = fib(n-1) + fib(n-2)
    return cache[n]


def main():
    init = time.clock()
    print fib(30)
    end = time.clock()
    delta = end - init
    print "Time spent: %s seconds." % delta

    init = time.clock()
    print fib(33)
    end = time.clock()
    delta = end - init
    print "Time spent: %s seconds." % delta

if __name__ == "__main__":
    main()