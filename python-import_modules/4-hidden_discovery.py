#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    for v in dir(hidden_4):
        if not v.startswith('__'):
            print(v)
