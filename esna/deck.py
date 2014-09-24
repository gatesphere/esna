#@+leo-ver=5-thin
#@+node:peckj.20140923100049.4066: * @file deck.py
#@@language python

#@+<< imports >>
#@+node:peckj.20140923100049.4067: ** << imports >>
import random
#@-<< imports >>
#@+<< declarations >>
#@+node:peckj.20140923100049.4068: ** << declarations >>
#@-<< declarations >>

#@+others
#@+node:peckj.20140923100049.4069: ** class Deck
class Deck:
  #@+others
  #@+node:peckj.20140923100049.4070: *3* __init__
  def __init__(self, cards):
    self.draw_deck = cards  # index 0 = top of deck
    self.discard_pile = []  # index 0 = top of deck
    self.shuffle()
  #@+node:peckj.20140923100049.4071: *3* shuffle
  def shuffle(self, cards_to_keep=0):
    ''' combines the discard + draw piles, and shuffles the decks '''
    self.combine_piles(cards_to_keep)
    random.shuffle(self.draw_deck)
  #@+node:peckj.20140924124512.4076: *4* combine_piles
  def combine_piles(self, cards_to_keep):
    self.draw_deck = self.draw_deck + self.discard_pile[cards_to_keep:]
    self.discard_pile = self.discard_pile[:cards_to_keep]
  #@+node:peckj.20140923100049.4072: *3* draw_card
  def draw_card(self):
    ''' draws the top card, and returns it '''
    c = self.draw_deck[0]
    self.draw_deck = self.draw_deck[1:]
    self.discard_card(c)
    return c
  #@+node:peckj.20140923100049.4073: *4* discard_card
  def discard_card(self, card):
    self.discard_pile = [card] + self.discard_pile
  #@+node:peckj.20140923100049.4074: *3* display
  def display(self):
    ''' debugging purposes only '''
    print 'draw: ', [x.reference for x in self.draw_deck]
    print 'discard: ', [x.reference for x in self.discard_pile]
    
  #@-others
#@-others
#@-leo
