#!/usr/bin/python3
import sys

if __name__ == '__main__':
    length = len(sys.argv)
    print('{} argument'.format(length) + 's' * int(length != 1))
    for i, v in enumerate(sys.argv):
        if i == 0:
            continue
        print('{}: {}'.format(i, v))
