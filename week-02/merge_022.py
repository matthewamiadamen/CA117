#!/usr/bin/env python3

import sys

def main():
  t1 = open(sys.argv[1],'r')
  t2 = open(sys.argv[2],'r')
  a = []

  for x, y in zip(t1,t2):
    x = x.strip()
    y = y.strip()
    a.extend([x, y])

  for i in a:
    print(i)
  t1.close()
  t2.close()

if __name__ == "__main__":
  main()
