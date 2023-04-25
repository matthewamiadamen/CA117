#!/usr/bin/env python3

def arithmetic(a, b, c=3, d=4):
   return a + b + c + d

print(arithmetic(1, 2, 5, 6))

print(arithmetic(3, 4, 5))

print(arithmetic(3, 4))

print(arithmetic(3, 4, d=3))

print(arithmetic(b=5, a=4, d=2, c=1))

print(arithmetic(a=2, b=4, 6))

print(arithmetic(6, a=2, b=4))

print(arithmetic(b=2, a=4, c=6))

print(arithmetic(b=5, 2, 5))
