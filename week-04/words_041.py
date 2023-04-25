#!/usr/bin/env python3

import sys
import string

text = ' '.join([n.strip() for n in sys.stdin.readlines()])

edit = ""
i = 0
while i < len(text) - 1:
  if text[i] not in string.punctuation:
    edit += text[i]
  elif text[i] in string.punctuation and ((text[i + 1] not in string.punctuation and text[i + 1] != " ") and (text[i - 1] not in string.punctuation and text[i - 1] != " ")):
    edit += text[i]
  i += 1

edit = edit.split(" ")
lol = edit[:]
dict = {}

for i in edit:
  if i not in lol:
    dict[i] = edit.count(i)
    lol = [n for n in lol if n != i]

print(dict)
dict = {n:
#dict = {n : edit.count(n) for n in edit if n not in edit[:edit.index(n)]}
#sorted = {n for n in sorted(dict.items())}

#for i, x in sorted:
 # print(f"{i} : {x}")
