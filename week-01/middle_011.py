#!/usr/bin/env python3

import sys

def middle(s):
  if len(s) % 2 == 0:
    return "No middle character!"
  else:
    return s[len(s) // 2]

for line in sys.stdin:
  line = line.strip()
  ans = middle(line)
  print(ans)
