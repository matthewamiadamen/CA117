#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip()
  i = 0
  if "m" in line:
    while line[i] != "m" and i < len(line):
      i += 1
    print(line[:i] + "M" + line[i + 1:])
  else:
    print(line)
