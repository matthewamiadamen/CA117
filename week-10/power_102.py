#!/usr/bin/env python3

def power(n, p):
  if p == 0:
    return 1
  else:
    return n * power(n, p-1)
