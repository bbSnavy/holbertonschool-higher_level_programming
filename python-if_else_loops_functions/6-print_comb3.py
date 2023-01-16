#!/usr/bin/python3
l = []
for x in range(10):
    for y in range(x, 10):
        l.append('%s%s' % (x, y))
print(', '.join(l) + 0 * '{:02}'.format(0))
