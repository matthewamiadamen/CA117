#!/usr/bin/env python3

class Queue(object):
  def __init__(self):
    self.q = []

  def enqueue(self, data):
    self.q.append(data)

  def dequeue(self):
    if len(self.q) != 0:
      return self.q.pop(0)
    else:
      return 'Error'

  def first(self):
    if len(self.q) != 0:
      return self.q[0]
    else:
      return 'Error'

  def is_empty(self):
    return len(self.q) == 0

  def __len__(self):
    return len(self.q)
