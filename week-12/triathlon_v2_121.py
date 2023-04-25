#!/usr/bin/env python3

class Triathlete(object):
  def __init__(self, name, tid):
    self.name = name
    self.tid = tid
    self.sporttime = {}
    self.totaltime = 0

  def __str__(self):
    return 'Name: {:}\nID: {:}\nRace time: {:}'.format(self.name, self.tid, self.totaltime)

  def add_time(self, sport, time):
    self.sporttime[sport] = time
    self.totaltime += time

  def get_time(self, sport):
    return self.sporttime[sport]

  def __eq__(self, other):
    return self.totaltime == other.totaltime

  def __lt__(self, other):
    return self.totaltime < other.totaltime

  def __gt__(self, other):
    return self.totaltime > other.totaltime

class Triathlon(object):
  def __init__(self):
    self.triathlon = {}

  def add(self, athlete):
    self.triathlon[athlete.tid] = athlete

  def remove(self, tid):
    del self.triathlon[tid]

  def lookup(self, tid):
    if tid in self.triathlon:
      return self.triathlon[tid]
    return None

  def __str__(self):
    output = ""
    for tid, athlete in sorted(self.triathlon.items(), key = lambda x: x[1].name):
      output += f"Name: {athlete.name}\nID: {athlete.tid}\n"
    return output
