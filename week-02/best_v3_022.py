#!/usr/bin/env python3

import sys

def main():
  try:
    beststudent = ""
    bestmark = 0
    largest = 0
    with open(sys.argv[1], 'r') as f:
      for i in f:
        i = i.strip()
        full = i.split(" ")
        try:
          mark = int(full[0])
        except ValueError:
          print(f"Invalid mark {full[0]} encountered. Skipping.")
          break
        student = ' '.join(full[1:])
        if int(mark > largest):
          largest = mark
          beststudent = student
          bestmark = mark
      print(f"Best student: {beststudent}")
      print(f"Best mark: {bestmark}")

  except FileNotFoundError:
    print("The file best_v3_input__00_022.txt could not be opened.")

if __name__ == "__main__":
  main()
