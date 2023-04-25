#!/usr/bin/env python3

import sys

for line in sys.stdin:
  i = 0
  while line[i] != ".":
    i += 1
  j = i + 1
  fn = line[:i].capitalize()
  while i < len(line) and not ("0" <= line[i] <= "9"):
    i += 1
  ln = line[j:i].capitalize()

  print(fn, ln)
