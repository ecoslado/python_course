__author__ = 'Enrique Coslado'

# Python's default arguments are evaluated once when the function is defined.

def foo(arg=list()):
    print arg
    arg.append("bar")

def foo2(arg=None):
    print arg
    if not arg:
        arg = list()
    arg.append("bar")

def main():
    print "A few calls to foo"
    foo()
    foo()
    foo()
    foo()

    print "A few calls to foo2"
    foo2()
    foo2()
    foo2()
    foo2()

if __name__ == "__main__":
    main()