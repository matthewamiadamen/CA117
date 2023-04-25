#!/usr/bin/env python3

class Student(object):
  def __init__(self, name, sid, modules = []):
    self.name = name
    self.sid = sid
    self.module = sorted([i[0] for i in modules])
    self.mark = round((sum([int(i[1]) for i in modules]) / len(modules)))

  def __str__(self):
    return f"Name: {self.name}\nID: {self.sid}\nModules: {', '.join(self.module)}\nAverage mark: {self.mark}"

