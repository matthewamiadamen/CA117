#!/usr/bin/env python3

class BankAccount(object):
  def __init__(self, balance = 0):
    self.balance = balance

  def deposit(self, amount):
      self.balance += amount

  def withdraw(self, withdraw):
    if self.balance - withdraw >= 0:
      self.balance -= withdraw

  def __str__(self):
    return 'Your current balance is {:.2f} euro'.format(self.balance)
