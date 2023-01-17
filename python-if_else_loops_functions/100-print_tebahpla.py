#!/usr/bin/python3
print('{}'.format(''.join(map(lambda v: v.upper() if ord(v) % 2 == 1 else v.lower(),
      reversed([chr(i) for i in range(ord('a'), ord('z') + 1)]))), end=''))
