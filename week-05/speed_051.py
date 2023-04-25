#!/usr/bin/env python3

import sys

numbers = [c.strip().split(" ") for c in sys.stdin.readlines()]
speeds = []

for c in numbers[1:]:
  currdist = int(numbers[numbers.index(c)][1])
  pastdist = int(numbers[numbers.index(c)-1][1])
  currtime = int(numbers[numbers.index(c)][0])
  pasttime = int(numbers[numbers.index(c)-1][0])
  if c == numbers[1:][0]:
    speeds.append(currdist // currtime)
  else:
    speeds.append((currdist - pastdist) // (currtime - pasttime))

print(max(speeds))
