#!/usr/bin/python3
import sys

if __name__ == '__main__':
    l = len(sys.argv)
    print('{} argument'.format(l) + 's' * int(l != 1))
    for i, v in enumerate(sys.argv):
        if i == 0:
            continue
        print('{}: {}'.format(i, v))
