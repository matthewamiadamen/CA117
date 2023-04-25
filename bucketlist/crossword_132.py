#!/usr/bin/env python3

import sys

lines = sys.stdin.readline()
lines = lines.lower().split()
a = lines[0]
b = lines[1]

for letter in a[::-1]:
  if letter in b:
    c = b.rfind(letter)
    d = a.rfind(letter)
    break
right_a = len(a) - d
left_a = d - 1

for i in range(len(a)):
  if i == d:
    print(b)
  else:
    print(f'{"." * left_a}{a[i]}{"." * right_a}')
