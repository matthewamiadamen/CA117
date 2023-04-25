#/usr/bin/env python3

import sys

line = [int(c.strip()) for c in sys.stdin.readlines()]

for i in line:
  if 0 < i <= 400:
    print(1)

  elif i == 0:
    print(0)

  elif i % 400 == 0:
    print(i // 400)

  else:
    print((i // 400) + 1)
