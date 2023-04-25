#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip()

  if line[-2:] == "ch" or line[-2:] == "sh":
    print(line + "es")

  elif line[-1] in ["x", "s", "z"]:
    print(line + "es")

  elif line[-2] not in ["a", "e", "i", "o", "u"] and line[-1] == "y":
    print(line[:-1] + "ies")

  elif line[-1] == "f":
    print(line[:-1] + "ves")

  elif line[-2:] == "fe":
    print(line[:-2] + "ves")

  elif line[-1] == "o":
    print(line + "es")

  else:
    print(line + "s")
