__author__ = 'jesus.pedro.gutierrez.almazan'

def flow_control_comprehension():
    numbers = range(10)
    print numbers
    numbers = [number for number in numbers if number < 5]
    print numbers

    numers_dict = {str(i):i for i in range(10) if i > 5}
    print numers_dict
    
def flow_control_others():
    if True:
        pass
    
    for i in range(10):
        if i == 5:
            continue
        print i
    print i

    for i in range(10):
        if i == 5:
            break
        print i
    print i
    
    for i in range(10):
        if i == 5:
            continue
        print i
    else:
        print 'colorin colorado'

    for i in range(10):
        if i == 5:
            break
        print i
    else:
        print 'colorin colorado'

def flow_control_generators():
    pass

def main():
    flow_control_comprehension()
    flow_control_others()

if __name__ == "__main__":
    main()
