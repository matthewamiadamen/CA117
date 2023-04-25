#!/usr/bin/env python3

def reverse(n, i = -1, q = None):
  if q == None:
    q = []
  if len(q) != len(n):
    q.append(n[i])
    return reverse(n, i - 1, q)
  else:
    return q
