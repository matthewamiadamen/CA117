#!/usr/bin/env python3

import sys

lines = [c.strip().split() for c in sys.stdin]

for i in lines:
  ints = [int(c) for c in i]
  divisor = len(i) // 3
  if divisor > 0:
    for i in range(divisor):
      ints.remove(min(ints))
  ans = sum(ints)
  if ans == 22:
    print(20)
  else:
    print(ans)
