#!/usr/bin/env python3

import sys

line = [line.strip() for line in sys.stdin]

word = [word for word in line if 'q' in word.lower() and "u" not in word.lower()[word.lower().index("q") + 1:]]

print(f"Words with q but no u: {word}")
