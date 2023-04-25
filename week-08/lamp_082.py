#!/usr/bin/env python3

class Lamp(object):

  def __init__(self, on = None):
    if on == None:
      self.on = False
    else:
      self.on = on

  def turn_on(self):
    self.on = True

  def turn_off(self):
    self.on = False

  def toggle(self):
    if self.on == True:
      self.on = False
    else:
      self.on = True
