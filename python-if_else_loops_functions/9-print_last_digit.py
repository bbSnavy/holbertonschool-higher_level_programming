#!/usr/bin/python3
def print_last_digit(number):
    try:
        r = str(int(str(number)))[-1]
        print(r, end='')
        return r
    except:
        return ''
