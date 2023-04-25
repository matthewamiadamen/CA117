#!/usr/bin/env python3

import sys

def contains(worda, wordb):
  for c in worda:
    if c not in wordb:
      return false
    else:
      wordb.replace(c, '', 1)
  return true

for line in sys.stdin:
  line  = line.strip().lower().split(" ")
  word1 = line[0]
  word2 = line[1]
  worda = list(word1)
  wordb = list(word2)

  flag = True
  for i in worda:
    if i in wordb:
      j = wordb.index(i)
      wordb.pop(j)
    else:
      flag = False
      break

  print(flag)
