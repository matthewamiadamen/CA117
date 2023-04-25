#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
numbers = lines[0].strip().split(" ")
letters = [c for c in lines[1].strip()]

new = {}
i = ord('A')
j = 0
while ord('A') <= i <= ord('F'):
  new[chr(i)] = numbers[j]
  i += 1
  j += 1

print(f"{' '.join([new[c] for c in letters if c in new])}")
