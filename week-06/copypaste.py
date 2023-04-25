#!/usr/bin/env python3

from sys import argv

lol = argv[1]

with open(lol, 'r') as f:
  file = f.readlines()

pasted = []
for i in file:
  i = i.rstrip()
  pasted.append(''.join([c for c in i if c != '\t']))

with open(lol, 'w') as g:
  for i in pasted:
    g.write(i)
