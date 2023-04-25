#!/usr/bin/env python3

import sys
import re

lines = sys.stdin.readlines()

max = 0
biggest = ''


for line in lines:
  line = line.strip()
  find = re.findall(r'aa|ee|oo|uu|ii', line.lower())
  count = len(find)
  if count > max:
    biggest = line
    max = count

print(biggest)
