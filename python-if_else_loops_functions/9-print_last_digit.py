#!/usr/bin/python3
def print_last_digit(number):
    try:
        print(str(int(str(number)))[-1], end='')
    except:
        pass
