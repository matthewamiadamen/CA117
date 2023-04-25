#!/usr/bin/env python3

class MP3Track(object):
  def __init__(self, title, duration, tracks = None):
    self.title = title
    self.duration = duration
    if tracks == None:
      self.tracks = []
    else:
      self.tracks = tracks

  def sectomin(self):
    minutes, seconds = divmod(self.duration, 60)
    return (minutes, seconds)

  def __str__(self):
    return f"Title: {self.title}\nBy: {', '.join(self.tracks)}\nDuration: {self.sectomin()[0]}:{self.sectomin()[1]:>02}"

