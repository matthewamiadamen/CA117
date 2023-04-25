#!/usr/bin/env python3

from math import sqrt

class Point(object):
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  def distance(self, other):
    return sqrt((self.x - other.x)** 2 + (self.y - other.y)** 2)

  def __str__(self):
    return '({:.1f}, {:.1f})'.format(self.x,self.y)
