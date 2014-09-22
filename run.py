#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:peckj.20140922102810.4097: * @file run.py
#@@first
#@@language python

#@+<< imports >>
#@+node:peckj.20140922102810.4098: ** << imports >>
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
  
  ## find a much better way of doing this
  
  levels = [4,10,None,3,None,1,5,None,2,8,None,9,6,7,None]
  bs = [0,15,27,9,14,2,14,20,9,10,29,29,8,24,17]
  gold = ['T',31,52,17,27,2,28,39,2,21,55,55,16,49,35]
  terrain = 'Forest'
  dungeon = False
  ref = 'J'
  paths = 0
  hit = 'head'
  monster = ('Typical',0)
  quest = ('Escort',2)
  events = { ('Forest','Forest'):     '+1',
             ('Forest','Desert'):     'B',
             ('Mountain','Desert'):   'H',
             ('Farm','Mountain'):     'M',
             ('Forest','Farm'):       'A',
             ('Mountain','Mountain'): 'G',
             ('Farm','Farm'):         'L',
             ('Desert','Desert'):     '+1' }
  
  c = Card(levels,bs,gold,terrain,dungeon,events,ref,paths,monster,quest,hit)
  
  deck.append(c)
  
#@-others

if __name__=='__main__':
  main()
#@-leo
