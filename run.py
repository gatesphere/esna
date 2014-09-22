#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:peckj.20140922102810.4097: * @file run.py
#@@first
#@@language python

#@+<< imports >>
#@+node:peckj.20140922102810.4098: ** << imports >>
import os
import csv

from esna.card import Card
#@-<< imports >>
#@+<< declarations >>
#@+node:peckj.20140922102810.4099: ** << declarations >>
deck = None
#@-<< declarations >>

#@+others
#@+node:peckj.20140922102810.4100: ** main
def main():
  initialize_deck()
  
  print deck[0].getTerrain()
  print deck[0].getMonsterType()
  print deck[0].getQuestLoot()
  print deck[0].getLevelIndex(1)
  pass
#@+node:peckj.20140922102810.4101: *3* initialize_deck
def initialize_deck():
  global deck
  deck = []
  
  #@+<< data reader code >>
  #@+node:peckj.20140922102810.4221: *4* << data reader code >>
  def comment_stripper(iterator):
    for line in iterator:
      if line.startswith('#'):
        continue
      if not line.strip():
        continue
      yield line

  def read_data(data_file):
    ''' a generator function for reading csv files with # comments. '''
    with open(data_file, 'rb') as csv_data:
      reader = csv.reader(comment_stripper(csv_data))
      for row in reader:
        yield row
  #@-<< data reader code >>
  
  for row in read_data('cards.dat'):
    c = create_card(row)
    deck.append(c)
  
#@+node:peckj.20140922102810.4220: *4* create_card
def create_card(row):
  levels = []
  for i in row[0:15]:
    if i == 'None':
      levels.append(None)
    else:
      levels.append(int(i))
  
  bs = [int(i) for i in row[15:30]]

  gold = []
  for i in row[30:45]:
    if i == 'T':
      gold.append('T')
    else:
      gold.append(int(i))

  terrain = row[45]
  dungeon = bool(row[46])
  ref = row[47]
  hit = row[48]
  paths = int(row[49])

  monster = (row[50], int(row[51]))
  quest = (row[52], int(row[53]))

  events = {}
  i = 54
  while i < 75:
    k = (row[i],row[i+1])
    v = row[i+2]
    events[k]=v
    i+=3
  
  c = Card(levels,bs,gold,terrain,dungeon,events,ref,paths,monster,quest,hit)
  return c
#@-others

if __name__=='__main__':
  main()
#@-leo
