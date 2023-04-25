#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
  censored = [n.strip() for n in f]

lines = [n.strip() for n in sys.stdin]
new = []

for censored in lines:
  swap = '@' * len(censored)
  new.append(lines.replace(censored, swap))

for i in new:
  print(i)
