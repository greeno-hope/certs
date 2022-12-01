import sys
import math
import getopt


def fermat(mod):
    '''
    Arrange n as a^2 - b^2 or (a-b)*(a+b)
    :param mod:
    :return:
    '''

    # Find the first perfect square above the root
    a = math.ceil(math.sqrt(mod))
    b = 0
    found = False

    while not found:
        a_sqr = math.pow(a, 2)
        b_sqr = a_sqr - mod
        if(b_sqr > 0):
            b = math.sqrt(b_sqr)
            if b.is_integer():
                found = True
            else:
                a = a + 1
        else:
            return mod, a, int(b), 0, 0

    return mod, a, int(b), int(a-b), int(a+b)

def modular(mod):
    '''
    Solving using the congruence - a^2 - b^2 = k.n
    :param mod:
    :return:
    '''

    pass

def run():
    res = None
    args = sys.argv
    if args[1] == '-f':
        res = fermat(int(args[2]))

    print(str(res))

if __name__ == '__main__':
    run()

