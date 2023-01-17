#!/usr/bin/python3
import sys

if __name__ == '__main__':
    length = len(sys.argv) - 1
    if length == 0:
        print('0 arguments.')
    else:
        print('{} argument'.format(length) + 's' * int(length != 1) + ':')
        for i, v in enumerate(sys.argv):
            if i == 0:
                continue
            print('{}: {}'.format(i, v))
