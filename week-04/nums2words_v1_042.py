#!/usr/bin/env python3

import sys

dict = {'1' : 'one',
        '2' : 'two',
        '3' : 'three',
        '4' : 'four',
        '5' : 'five',
        '6' : 'six',
        '7' : 'seven',
        '8' : 'eight',
        '9' : 'nine',
        '0' : 'zero',
        '10' : 'ten'}

for line in sys.stdin.readlines():
  line = line.strip().split(" ")
  print(f"{' '.join([dict[c] for c in line if c in dict])}")
