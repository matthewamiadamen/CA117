#!/usr/bin/env python3

class BankAccount(object):

  def set_attributes(self, name, number, balance, deposit = None):
    if deposit == None:
      self.balance = balance
    else:
      self.balance = balance + deposit

    self.name = name
    self.number = number

  def print_attributes(self):
    print('Name: {:}'.format(self.name))
    print('Account number: {:}'.format(self.number))
    print('Balance: {:.2f}'.format(self.balance))

  def deposit(self, deposit):
    self.balance += deposit 
