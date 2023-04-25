#!/usr/bin/env python3

class Score(object):
  def __init__(self, goal = 0, point = 0):
    self.goals = goal
    self.points = point

  def __str__(self):
    return '{:} goal(s) and {:} point(s)'.format(self.goals, self.points)
