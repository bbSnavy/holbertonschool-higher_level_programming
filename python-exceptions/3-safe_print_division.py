#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except:
        return None
    finally:
        if b == 0:
            print('Inside result: None')
        else:
            print('Inside result: %s' % (a / b))
