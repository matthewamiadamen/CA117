#!/usr/bin env python3

import sys

def main():
  f = open('dictionary05.txt', 'r')

  words = [line.strip() for line in f.readlines()]
  I7words = [word for word in words if len(word.lower()) == 17]
  I8plus = [word for word in words if len(word.lower()) >= 18]
  fouras = [word for word in words if len([n for n in word.lower() if n == 'a']) == 4]
  more2q = [word for word in words if len([n for n in word.lower() if n == 'q']) >= 2]
  cie = [word for word in words if 'cie' in word.lower()]
  angle = [word for word in words if [n for n in 'angle' if n in word.lower()] and len(word) == 5]

  print(f"Words containing 17 letters: {I7words}")
  print(f"Words containing 18+ letters: {I8plus}")
  print(f"Words with 4 a's: {fouras}")
  print(f"Words with 2+ q's: {more2q}")
  print(f"Words containing cie: {cie}")
  print(f"Anagrams of angle: {angle}")

  f.close()

if __name__ == '__main__':
  main()
