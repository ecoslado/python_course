__author__ = 'kike'
import time

cache = dict()

def cached(function):
    def wrapper(key):
        if key not in cache:
            cache[key] = function(key)
        return cache[key]
    return wrapper

@cached
def fib(n):
    return 1 if n < 2 else fib(n-1) + fib(n-2)


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