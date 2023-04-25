#!/usr/bin/env python3

class Stack(object):
  def __init__(self):
    self.l = []

  def push(self, data):
    self.l.append(data)

  def pop(self):
    if len(self.l) != 0:
      return self.l.pop()
    else:
      return 'Error'

  def top(self):
    if len(self.l) != 0:
      return self.l[-1]
    else:
      return 'Error'

  def is_empty(self):
    return len(self.l) == 0

  def __len__(self):
    return len(self.l)
