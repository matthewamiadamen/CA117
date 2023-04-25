#!/usr/bin/env python3

import sys

def capitalise(s):
  return s[0].upper() + s[1:len(s) - 1] + s[len(s) - 1].upper()

for line in sys.stdin:
  line = line.strip()
  capitalised = capitalise(line)
  print(capitalised)
