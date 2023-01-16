#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10 * (-1 if number < 0 else 1)
text = (
    lambda n: ['greater than 5', 'less than 6 and not 0'][n < 6]
    if n != 0 else '0')(digit)
print(
    f"Last digit of {number} is {digit} and is {text}")
