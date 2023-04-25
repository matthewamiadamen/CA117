#!/usr/bin/env python3

class Meeting(object):
  def __init__(self, hour = 0, minute = 0, duration = 0):
    self.hour = hour
    self.minute = minute
    self.duration = duration

  def __str__(self):
    return f"{self.hour:>02d}:{self.minute:>02d} ({self.duration} minutes)"

class Schedule(object):
  def __init__(self):
    self.schedule = []

  def add(self, meeting):
    if meeting not in self.schedule:
      self.schedule.append(meeting)

  def __str__(self):
    meetingstring = sorted([f'{c.hour:>02d}:{c.minute:>02d} ({c.duration} minutes)' for c in self.schedule])
    return "Schedule\n--------\n"\
     + "\n".join([c for c in meetingstring])\
      + f"\nMeetings today: {len(self.schedule)}"
