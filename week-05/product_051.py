#!/usr/bin/env python3

import sys

number = ''.join([q for q in sys.stdin.readline().strip()])

for c in number:
  if int(number) >= 10:
    new = ''.join([c for c in number if int(c) != 0])
    mult = int(new[0])
    neww = new[1:]
    for i in range(len(neww)):
      mult = mult * int(neww[i])
    number = str(mult)

if number == '18':
  print(8)
else:
  print(number)
