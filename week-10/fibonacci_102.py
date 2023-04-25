#!/usr/bin/env python3

def fibonacci(n, fib = [1,1], coun = 0):
  if n == 0 or n == 1:
    return 1
  elif coun <= n:
    curr = fib[-1] + fib[-2]
    fib.append(curr)
    return fibonacci(n, fib, coun + 1)
  else:
    return fib[n]
