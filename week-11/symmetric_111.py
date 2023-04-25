#!/usr/bin/env python3

import sys

names = [c.strip() for c in sys.stdin.readlines()]
holder = []

for i in range(0, len(names)//2):
   if len(names[i]) == len(names[i + 1]):
     new = names[i + 1]
     names.pop(i + 1)
     holder.append(new)
ans = names + holder[::-1]

#print(f"{'\n'.join([c for c in names])}")
for c in ans:
  print(c)
