#!/usr/bin/env python3

import sys

def tagger(item):
  return item[1]

vowels = 'aeiou'

text = ' '.join([n.strip().lower() for n in sys.stdin.readlines()])

dict = {vowel: text.count(vowel) for vowel in vowels}
max = max([len(str(v)) for k, v in dict.items()])

for k, v in sorted(dict.items(), key=tagger, reverse = True):
  print(f"{k} : {v:>{max}}")
