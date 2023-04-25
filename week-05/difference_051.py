#!/usr/bin/env python3

import sys

lines = [c.strip() for c in sys.stdin.readlines()]

line = ''.join(['-' if (c == j) else '*' for c, j in zip(lines[0], lines[1])])
for i in lines:
  print(i)
print(line)
