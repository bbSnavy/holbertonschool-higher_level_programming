#!/usr/bin/python3
from add_0 import add

if __name__ == '__main__':
    a = 1
    b = 2
    print('%s + %s = %s' % (a, b, add(a, b)) + 0 * '{}'.format(0))
