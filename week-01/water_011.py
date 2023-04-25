#!usr/bin/env python3

import sys
buckets = []
char = ""

lines = sys.stdin.readlines()

total = int(lines[0].strip())
b = lines[1].strip().split(" ")

i = 0
while i < len(b):
  char = int(b[i])
  buckets.append(char)
  i += 1

amount = 0
i = 0
while i < len(buckets) and amount + buckets[i] <= total:
  amount = amount + buckets[i]
  i += 1
print(i)
