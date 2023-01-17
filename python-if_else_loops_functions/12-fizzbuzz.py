#!/usr/bin/python3
def fizzbuzz(i=1):
    if i > 100:
        return
    print({'00': str(i), '01': 'Fizz', '10': 'Buzz'}
          .get('%d%d' % (i % 5 == 0, i % 3 == 0), 'FizzBuzz'), end=' ')
    fizzbuzz(i + 1)
