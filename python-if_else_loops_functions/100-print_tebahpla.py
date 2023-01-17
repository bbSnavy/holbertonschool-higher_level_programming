#!/usr/bin/python3
exec("print('{}'.format(''.join(map(lambda v: v.upper() if ord(v) % 2 == 1 el\
se v.lower(), reversed([chr(i) for i in range(ord('a'), ord('z') + 1)])))), e\
nd='')")
