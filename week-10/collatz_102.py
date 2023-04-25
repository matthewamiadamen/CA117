#!/usr/bin/env python3

def collatz(n):
  print(n)
  if n != 1:
    if n % 2 == 0:
      return collatz(n // 2)
    else:
      return collatz((n * 3) + 1)
  else:
    return 1
