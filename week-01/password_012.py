#!/usr/bin/env python3

import sys

for line in sys.stdin:
  d = 0
  lc = 0
  uc = 0
  sc = 0
  total = 0
  line = line.strip()
  for i in line:
    if "a" <= i <= "z" and lc < 1:
      lc += 1
      total += 1
    elif "0" <= i <= "9" and d < 1:
      d += 1
      total += 1
    elif "A" <= i <= "Z" and uc < 1:
      uc += 1
      total += 1
    elif uc == 0 and lc == 0 and d == 0 and sc < 1:
      sc += 1
      total += 1
  print(total)
