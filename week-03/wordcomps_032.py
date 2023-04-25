#!/usr/bin/env python3

import sys

vowels = "aeiou"
lines = [n.strip() for n in sys.stdin]

print(f"Shortest word containing all vowels: {sorted([n for n in lines if len([char for char in vowels if char in n.lower()]) == 5], key = len)[0]}")
print(f"Words ending in iary: {len([n for n in lines if n.lower()[-4:] == 'iary'])}")
maxcount = max([word.lower().count('e') for word in lines])
print(f"Words with most e's: {[n for n in lines if n.lower().count('e') == maxcount]}")
