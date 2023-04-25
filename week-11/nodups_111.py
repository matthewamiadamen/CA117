#!/usr/bin/env python3

import re
import sys

lines = sys.stdin.read().strip()

#words = re.findall(r'\b\w+\b', lines.lower())
words = set()
for match in re.finditer(r'\b\w+\b', lines):
  word = match.group().lower()
  if not (len(word) == 1 and not word == 'a'):
    if word in words:
      lines = lines[:match.start()] + '. ' + lines[match.end()+1:]
    else:
      words.add(word)

print(lines)

