#!/usr/bin/env python3

class Student(object):
  def __init__(self, sid, name, modlist = None):
    if modlist != None:
      self.modlist = [c for c in modlist][::-1]
    else:
      self.modlist = []
    self.name = name
    self.sid = sid

  def __str__(self):
    return f"ID: {self.sid}\nName: {self.name}\nModules: {', '.join([c for c in self.modlist])}"

  def add_module(self, newmod):
    if newmod not in self.modlist:
      self.modlist.append(newmod)

  def del_module(self, delmod):
    if delmod in self.modlist:
      self.modlist.remove(delmod)
