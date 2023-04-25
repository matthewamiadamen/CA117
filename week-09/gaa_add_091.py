#!/usr/bin/env python3

class Score(object):
  def __init__(self, goal = 0, point = 0):
    self.goals = goal
    self.points = point

  def __str__(self):
    return '{:} goal(s) and {:} point(s)'.format(self.goals, self.points)

  def __eq__(self, other):
    return self.goals_to_point() == other.goals_to_point()

  def goals_to_point(self):
    return (self.points + (self.goals * 3))

  def __lt__(self, other):
    return self.goals_to_point() < other.goals_to_point()

  def __le__(self, other):
    return self.goals_to_point() <= other.goals_to_point()

  def __gt__(self, other):
    return self.goals_to_point() > other.goals_to_point()

  def __ge__(self, other):
    return self.goals_to_point() >= other.goals_to_point()

  def __ne__(self, other):
    return not self.goals_to_point() == other.goals_to_point()

  def __add__(self, other):
    return Score(self.goals + other.goals, self.points + other.points)

  def __iadd__(self, other):
    self.goals += other.goals
    self.points += other.points
    return self
