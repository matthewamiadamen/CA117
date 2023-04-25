#!/usr/bin/env python3

class Element(object):

  def set_attributes(self, number, name, symbol, bp):
    self.number = number
    self.name = name
    self.symbol = symbol
    self.bp = bp

  def print_attributes(self):
    print('Number: {:}'.format(self.number))
    print('Name: {:s}'.format(self.name))
    print('Symbol: {:s}'.format(self.symbol))
    print('Boiling point: {:} K'.format(self.bp))
