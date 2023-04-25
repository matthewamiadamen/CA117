#!/usr/bin/env python3

class matcher(object):
  def __init__(self, test = None):
    self.l = []
    if test != None:
      self.test = [c for c in test]

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

  def __str__(self):
    for i in self.test:
      if i == '(':
        self.l.append(i)
      elif i == ')':
        try:
          self.l.pop()
        except IndexError:
          return 'False'

      elif i == '{':
        self.l.append(i)
      elif i == '}':
        if '{' in self.l:
          self.l.pop()

      elif i == '[':
        self.l.append(i)
      elif i == ']':
        if '[' in self.l:
          self.l.pop()
    if len(self.l) == 0:
      return 'True'
    else:
      return 'False'
