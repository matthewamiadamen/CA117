#!/usr/bin/env python3

import sys

line = sys.stdin.readlines()
total = 0
lol = 3
for i in line:
  i = i.strip().split(" ")
  club = "".join(i[1:-8])
  if len(club) > total:
    total = len(club)

print(f'{"POS":<3s} {"CLUB":<{total}s} {"P":>3s}\
 {"W":>3s} {"D":>3s} {"L":>3s} {"GF":>3s} {"GA":>3s} \
{"GD":>3s} {"PTS":<3s}')

for i in line:
  i = i.strip().replace("\t", "").split(" ")
  lol = " ".join(i[1:-8])

  print(f'{i[0]:>3s} {lol:<{total + 1}s} {i[-8]:<2s}\
  {i[-7]:<2s} {i[-6]:<s} {i[-5]:<2s} {i[-4]:<2s}\
  {i[-3]:<2s} {i[-2]:<3s}{i[-1]:>3s}')
