#!/usr/bin/env python3

class Student(object):
  def __init__(self, name, sid, modules = []):
    if modules != []:
      self.module = sorted([i[0] for i in modules])
    else:
      self.module = modules
    self.name = name
    self.sid = sid
    self.mark = round((sum([int(i[1]) for i in modules]) / len(modules)))

  def __str__(self):
    return f"Name: {self.name}\nID: {self.sid}\nModules: {', '.join(self.module)}\nAverage mark: {self.mark}"

class Classlist(object):
  def __init__(self):
    self.list = []

  def add(self, student):
    self.list.append(student)

  def __str__(self):
    sortedlist = sorted([f"Name: {c.name}\nID: {c.sid}\nModules: {', '.join(c.module)}\nAverage mark: {c.mark}" for c in self.list])
    return '\n'.join(sortedlist)
