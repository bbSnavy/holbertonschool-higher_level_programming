#!/usr/bin/python3
exec("print(', '.join(list(dict([(''.join(sorted(set(list(v)), key=int)), v) \
for v in sorted([v for v in ['{:02}'.format(i) for i in range(100)] if (l\
ambda a: len(set(list(a))) == 2)(v)], key=int)]).keys())))")
