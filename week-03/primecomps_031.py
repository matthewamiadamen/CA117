#!/usr/bin/env python3

import sys

def primecomps(s):
  primecomps = [n for n in range(2, s + 1)]
  prime = []
  for q in primecomps:
    flag = True
    t = [u for u in range(2, q)]
    for i in t:
      if q % i == 0:
        flag = False
        break

    if flag == True:
      prime.append(q)

  print(f"Primes: {prime}")

for i in sys.stdin:
  i = int(i.strip())
  primecomps(i)
