#!/usr/bin/env python3

class Contact(object):
  def __init__(self, name, phone, email):
    self.name = name
    self.phone = phone
    self.email = email

class Contactlist(object):
  def __init__(self):
    self.contactlist = {}

  def add(self, newcontact):
    if newcontact.name not in self.contactlist:
      self.contactlist[newcontact.name] = newcontact

  def remove(self, name):
    self.contactlist.pop(name)

  def get(self, name):
    if name in self.contactlist:
      return self.contactlist[name]
    else:
      return None

  def __str__(self):
    contacts = sorted(self.contactlist.items())
    list = []
    for k, contact in contacts:
      list.append(f'{contact.name} {contact.phone} {contact.email}')
    return "Contact list\n------------\n" +'\n'.join([c for c in list])
