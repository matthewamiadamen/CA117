#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip().lower()
  alphabet = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])

  ans = ''.join([c for c in alphabet if c not in line])
  if len(ans) == 0:
    print('pangram')
  else:
    print(f"missing {ans}")
