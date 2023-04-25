#!/usr/bin/env python3

import sys

def swap_keys_values(dict):
  new = [[v, c] for c, v in dict.items()]
  print(new)
