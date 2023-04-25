#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip().upper()
  words = line.split(" ")

  if words[0] in words[1]:
    print("True")
  else:
    print("False")
