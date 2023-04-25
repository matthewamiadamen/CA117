#!/usr/bin/env python3

import sys
import calendar
poem = {"Monday": "Monday's child is fair of face.",
        "Tuesday": "Tuesday's child is full of grace.",
        "Wednesday": "Wednesday's child is full of love.",
        "Thursday": "Thursday's child has far to go.",
        "Friday": "Friday's child is loving and giving.",
        "Saturday": "Saturday's child works hard for a living.",
        "Sunday": "Sunday's child is fair and wise and good in every way."}

for line in sys.stdin:
  line = line.strip().split(" ")
  day = calendar.weekday(int(line[2]), int(line[1]), int(line[0]))
  print(f'You were born on a {calendar.day_name[day]} and {poem[calendar.day_name[day]]}')
