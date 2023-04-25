#!/usr/bin/env python3

import sys

def recomps(s):
  recomp = [n for n in range(1, s + 1)]
  print(f"Non-multiples of 3 replaced: {[n if n % 3 == 0 else 0 for n in recomp]}")

for i in sys.stdin:
  i = int(i.strip())
  recomps(i)
