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

class MP3Collection(object):
  def __init__(self):
    self.collection = {}

  def add(self, track):
    self.collection[track.title] = track

  def remove(self, title):
    del self.collection[title]

  def __add__(self, other):
    new = MP3Collection()
    for k, v in self.collection.items():
      if k not in other.collection:
        new.add(v)
    for k, v in other.collection.items():
      new.add(v)
    return new

  def lookup(self, title):
    if title in self.collection:
      return self.collection[title]
