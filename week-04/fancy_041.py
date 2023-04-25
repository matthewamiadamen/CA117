#!/usr/bin/env python3

import sys

def finder(s, dict):
  if i in contacts:
    print(f"Phone: {dict[s][0]}")
    print(f"Email: {dict[s][1]}")
  else:
    print("No such contact")

with open(sys.argv[1], 'r') as f:
  lines = [n.strip().split(" ") for n in f.readlines()]

  contacts = {line[0] : [line[1], line[2]] for line in lines}

  key = [n.strip() for n in sys.stdin]
  for i in key:
    print(f"Name: {i}")
    finder(i, contacts)
