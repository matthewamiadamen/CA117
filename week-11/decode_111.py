#!/usr/bin/env python3

import sys
lines = [c.strip() for c in sys.stdin.readlines()]

for line in lines:
  for let in range(0, len(line)):
    if line[let] in ['a','e','i','o','u'] and (let + 2) <= len(line):
      new = list(line).pop(let)
      new = ''.join(line)
      new = list(line).pop(let)
      new = ''.join(line)
      print(new)

for c in lines:
  print(c)
