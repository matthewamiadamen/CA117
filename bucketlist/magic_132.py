#!/usr/bin/env python3

import sys

def magicnum(k):
  magicc = 0
  j = 3
  while True:
    if all(c in ["3", "9"] for c in str(j)):
      magicc = magicc + 1
    if magicc == k:
      return j
    j = j + 1

if __name__ == "__main__":
  k = int(sys.stdin.readline().strip())
  ans = magicnum(k)
  print(ans)
