#!/usr/bin/python3
def uppercase(str):
    r = []
    for c in str:
        v = ord(c)
        if v >= ord('a') and v <= ord('z'):
            r.append(chr(v - 32))
        else:
            r.append(chr(v))
    print('{}'.format(''.join(r)))
