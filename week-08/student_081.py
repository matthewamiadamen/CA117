#!/usr/bin/env python3

class Student(object):
  def set_attributes(self, sid, name, modlist = []):
    self.name = name
    self.sid = sid
    self.modlist = modlist

  def print_attributes(self):
    print('ID: {:}'.format(self.sid))
    print('Name: {:}'.format(self.name))
    print('Modules: {:}'.format(', '.join([c for c in self.modlist])) )

  def add_module(self, newmod):
    if newmod not in self.modlist:
      self.modlist.append(newmod)

  def del_module(self, delmod):
    if delmod in self.modlist:
      self.modlist.remove(delmod)
