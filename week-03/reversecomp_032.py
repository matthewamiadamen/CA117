#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
reverse = []

def reversed(line):
  i = 0
  j = len(reverse) - 1

  while i <= j:
    a = (i + j) // 2
    if reverse[a].lower() < line:
      i = a + 1
    else:
      j = a
  return reverse[i].lower() == line

reverse = [n.strip().lower() for n in sys.stdin if len(n.strip()) >= 5]

lol = [n for n in reverse if reversed(n[::-1].lower())]
print(lol)
