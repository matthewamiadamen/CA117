#!/usr/bin/env python3

from math import sqrt
import sys

def findroots(a, b, c):
  try:
    posroot = ((-1 * b) + sqrt((b ** 2) - ((4 * a)* c)) ) / (2 * a)
    negroot = ((-1 * b) - sqrt((b ** 2) - ((4 * a) * c)) ) / (2 * a)
    print(f"{negroot:.1f}, {posroot:.1f}")
  except ValueError:
    print(None)

for line in sys.stdin.readlines():
  roots = line.strip().split(" ")
  findroots(int(roots[0]), int(roots[1]), int(roots[2]))
