#!/usr/bin/env python3

import sys

line = sys.stdin.readlines()
start = line[0].strip()
swaps = line[1].strip()


cups = ['cup1', 'cup2', 'cup3']
cups[int(start) - 1] = 'mycup'

def swapper(i, cups):
  if i == 'A':
    tmp = cups[0]
    cups[0] = cups[1]
    cups[1] = tmp
    return cups

  elif i == 'B':
    tmp = cups[1]
    cups[1] = cups[2]
    cups[2] = tmp
    return cups

  elif i == 'C':
    tmp = cups[0]
    cups[0] = cups[2]
    cups[2] = tmp
    return cups

for i in swaps:
  swapper(i, cups)

print(cups.index('mycup') + 1)
