#!/usr/bin env python3

def get_divisors(s):
  allc = [i for i in range(1, int(s) + 1)]
  divisors = [c for c in allc if int(s) % c == 0]
  return divisors

def get_proper_divisors(s):
  return get_divisors(s)[:len(get_divisors(s)) - 1]

def is_perfect(s):
  total = sum(get_proper_divisors(s))
  if total == int(s):
    return True
  return False
