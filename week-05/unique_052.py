#!/usr/bin/env python3

import sys

txt = sys.stdin.readlines()
numbers = [c.strip() for c in txt]

for c in numbers:
  n = c.split(" ")
  n = [int(q) for q in n]
  n.sort()
  highest = 0
  flag = True

  for i in n:
    if n.count(i) == 1:
      highest = i
      flag = False

  if flag == True:
    print("none")
  else:
    print(highest)
