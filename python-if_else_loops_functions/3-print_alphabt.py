#!/usr/bin/python3
print(("{}" * 26)
      .format(*[chr(i) for i in range(97, 123) if i not in [101, 113]]), end='')
