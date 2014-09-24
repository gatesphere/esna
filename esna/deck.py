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
  #@+node:peckj.20140924124512.4079: *3* basic interaction
  #@+node:peckj.20140923100049.4071: *4* shuffle
  def shuffle(self, cards_to_keep=0):
    ''' combines the discard + draw piles, and shuffles the decks '''
    self.combine_piles(cards_to_keep)
    random.shuffle(self.draw_deck)
  #@+node:peckj.20140924124512.4076: *5* combine_piles
  def combine_piles(self, cards_to_keep):
    self.draw_deck = self.draw_deck + self.discard_pile[cards_to_keep:]
    self.discard_pile = self.discard_pile[:cards_to_keep]
  #@+node:peckj.20140923100049.4072: *4* draw_card
  def draw_card(self, cards_to_keep=0):
    ''' draws the top card, and returns it '''
    if len(self.draw_deck) == 0:
      self.shuffle(cards_to_keep)
    c = self.draw_deck[0]
    self.draw_deck = self.draw_deck[1:]
    self.discard_card(c)
    return c
  #@+node:peckj.20140923100049.4073: *5* discard_card
  def discard_card(self, card):
    self.discard_pile = [card] + self.discard_pile
  #@+node:peckj.20140924124512.4080: *3* advanced interaction
  #@+node:peckj.20140924124512.4082: *4* draw_battle_strength
  def draw_battle_strength(self, p_level, e_level):
    if len(self.discard_pile) < 1:
      card1 = self.draw_card()
    else:
      card1 = self.discard_pile[0]
    
    card2 = self.draw_card(1)
    card3 = self.draw_card(2)
    
    p_bs = card1.get_bs(card2.get_level_index(p_level))
    e_bs = card2.get_bs(card3.get_level_index(e_level))
    
    return (p_bs, e_bs)
  #@+node:peckj.20140924124512.4083: *4* draw_loot_value
  def draw_loot_value(self, e_level):
    if len(self.discard_pile) < 1:
      card1 = self.draw_card()
    else:
      card1 = self.discard_pile[0]
    
    card2 = self.draw_card(1)
    
    loot_value = card1.get_gold(card2.get_level_index(e_level))
    return loot_value
  #@+node:peckj.20140924124512.4084: *4* draw_kingdom
  def draw_kingdom(self):
    paths = self.draw_card().get_paths()
    t1 = self.draw_card().get_terrain()
    t2 = self.draw_card().get_terrain()
    
    return (paths, t1, t2)
  #@+node:peckj.20140924124512.4085: *4* draw_events
  def draw_events(self, t1, t2):
    c = self.draw_card()
    
    dungeon = False
    if c.get_terrain() in [t1,t2]:
      dungeon = c.get_dungeon()
    
    events = c.get_events()
    key = (t1, t2)
    e = events.get(key, False)
    if not e:
      key = (t2, t1)
      e = events.get(key, False)
    
    return (dungeon, e)
  #@+node:peckj.20140924124512.4086: *4* draw_quest ##todo
  def draw_quest(self):
    pass # complicated, do it later
  #@+node:peckj.20140924124512.4087: *4* draw_treasure
  def draw_treasure(self):
    c = self.draw_card()
    t_type = c.get_monster_type()
    return t_type
  #@+node:peckj.20140924124512.4089: *4* draw_monster
  def draw_monster(self):
    m_type = self.draw_card().get_monster_type()
    pos_terrain = self.draw_card().get_terrain()
    neg_terrain = self.draw_card().get_terrain()
    m_loot = self.draw_card().get_monster_loot()
    
    return (m_type, pos_terrain, neg_terrain, m_loot)
  #@+node:peckj.20140924124512.4081: *3* debugging
  #@+node:peckj.20140923100049.4074: *4* display
  def display(self):
    ''' debugging purposes only '''
    print 'draw: ', [x.reference for x in self.draw_deck]
    print 'discard: ', [x.reference for x in self.discard_pile]
    
  #@-others
#@-others
#@-leo
