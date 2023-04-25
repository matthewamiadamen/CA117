#!/usr/bin/env python3

def count(n, coun = 0):
  if n != '':
    return count(n[:-1], coun + 1)
  else:
    return coun
