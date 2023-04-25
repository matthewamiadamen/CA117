#!/usr/bin/env python3

import sys
total = 0
line = sys.stdin.readlines()

for i in line:
  i = i.strip()
  if len(i) > total:
    total = len(i)

for i in line:
  i = i.strip()
  print(f'{i:^{total}s}')
