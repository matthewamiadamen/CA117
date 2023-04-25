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
        '10' : 'ten',
        '0' : 'zero'}

for line in sys.stdin.readlines():
  line = line.strip().split(" ")
  print(f"{' '.join([dict[c] if c in dict else 'unknown' for c in line])}")
