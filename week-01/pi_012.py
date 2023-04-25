#!/usr/bin/env python3

import sys
import math

for line in sys.stdin:
  line = line.strip()
  line = int(line)
  print(f'{math.pi:.{line}f}')
