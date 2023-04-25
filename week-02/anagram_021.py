#!/usr/bin/env python3
import sys

for lines in sys.stdin:
  lines = lines.strip()
  lines = lines.split(" ")

  for i in lines[0]:
    if len(lines[0]) == len(lines[1]) and i in lines[1]:
      lines[1] = lines[1].replace(i, " ", 1)
      flag = True

    else:
      flag = False
      break
  print(flag)
