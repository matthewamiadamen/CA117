#!/usr/bin/env python3

class Point(object):

  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  def midpoint(self, other):
    return Point(((self.x + other.x)/2), ((self.y + other.y)/2))

  def __str__(self):
    return '({:.1f}, {:.1f})'.format(self.x, self.y)

class Circle(object):
  def __init__(self,centre = None, radius = 1):
    if centre == None:
      self.centre = Point()
    else:
      self.centre = centre
    self.radius = radius

  def __str__(self):
    return 'Centre: {:}\nRadius: {:}'.format(self.centre, self.radius)
