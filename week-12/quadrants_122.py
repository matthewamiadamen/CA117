#!/usr/bin/env python3

import sys

lines = [(c.strip().split()) for c in sys.stdin.readlines()]

for c in lines:
  if int(c[0]) > 0 and int(c[1]) > 0:
    print(1)
  elif int(c[0]) < 0 and int(c[1]) > 0:
    print(4)
  elif int(c[0]) > 0 and int(c[1]) < 0:
    print(2)
  else:
    print(3)
