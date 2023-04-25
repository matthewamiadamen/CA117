#!/usr/bin/env python3

import sys
import string

lines = sys.stdin.read().strip().lower()
punc = string.punctuation
text = ""
unique = 0

for i in lines:
  if i not in punc:
    text += i

text = text.split(" ")
for i in text:
  counter = text.count(i)
  if counter == 1:
    unique += 1
print(unique + 48)
