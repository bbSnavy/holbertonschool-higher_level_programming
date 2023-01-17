#!/usr/bin/python3
def fizzbuzz(i=1):
    if i > 100:
        print()
        return
    k = '%d%d' % (i % 5 == 0, i % 3 == 0)
    v = {
        '00': str(i),
        '01': 'Fizz',
        '10': 'Buzz',
    }.get(k, 'FizzBuzz')
    print(v, end=' ')
    fizzbuzz(i + 1)
