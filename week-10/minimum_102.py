#!/usr/bin/env python3

def minimum(n):
  if len(n) > 1:
    max = 0
    for i in n:
      if i > max:
        max = i
    return minimum([c for c in n if c != max])
  else:
    return ''.join([str(c) for c in n])
