#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
  lines = [c.strip().split(" ") for c in f.readlines()]
  cmon = [[c[0], c[1]] for c in lines]
  cmon2 = {str(c) : cmon[c] for c in range(0, 11)}

  for line in sys.stdin.readlines():
    line = line.strip().split(" ")
    line = [c for c in line if c in cmon2]
    print(f"{' '.join([cmon2[c][1] if c in cmon2 else 'unknown' for c in line])}")
