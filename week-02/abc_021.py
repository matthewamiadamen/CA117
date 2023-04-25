#!/usr/bin/env python3

import sys

line = sys.stdin.readline().strip().split(" ")
intline = [int(i) for i in line]
sorted = sorted(intline)

dict = { "A": sorted[0],
         "B": sorted[1],
         "C": sorted[2],}

abc = sys.stdin.readline().strip()

print(f'{dict[abc[0]]} {dict[abc[1]]} {dict[abc[2]]}')
