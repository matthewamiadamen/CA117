#!/usr/bin/env python3

def maximum(n):
  if len(n) > 1:
    smallest = n[0]
    for i in n[1:]:
      if i < smallest:
        smallest = i
    return maximum([c for c in n if c != smallest])
  else:
    return ''.join([str(c) for c in n])
