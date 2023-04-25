#!/usr/bin/env python3

import sys

for lines in sys.stdin:
  a = ""
  lines = lines.strip().lower()
  for i in lines:
    if "a" <= i <= "z" or "0" <= i <= "9":
      a += i
  j = 0
  for i in a:
    if i == a[len(a) - 1 - j]:
      j += 1
      flag = True

    else:
      flag = False
      break
  print(flag)
