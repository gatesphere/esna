#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:peckj.20140922102810.4097: * @file run.py
#@@first
#@@language python

#@+<< imports >>
#@+node:peckj.20140922102810.4098: ** << imports >>
import os

from esna.card import Card
from esna.datareader import read_data
from esna.deck import Deck
#@-<< imports >>
#@+<< declarations >>
#@+node:peckj.20140922102810.4099: ** << declarations >>
card_data = 'cards.dat'

#@-<< declarations >>

#@+others
#@+node:peckj.20140922102810.4100: ** main
def main():
  deck = initialize_deck()
  
  deck.display()
  
  c = deck.draw_card()
  
  print c.getTerrain()
  print c.getMonsterType()
  print c.getQuestLoot()
  print c.getLevelIndex(1)

  deck.display()
#@+node:peckj.20140922102810.4101: *3* initialize_deck
def initialize_deck():
  cards = []
  
  for row in read_data(card_data):
    c = create_card(row)
    cards.append(c)
  
  return Deck(cards)
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
