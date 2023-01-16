#!/usr/bin/python3

r = ['{:02}'.format(i) for i in range(100)]

r = [v for v in r if (lambda a: len(set(list(a))) == 2)(v)]

r = sorted(r, key = int)

r = [(''.join(sorted(set(list(v)), key=int)), v) for v in r]

r = dict(r)

r = list(r.keys())

r = ', '.join(r)
print(r)
