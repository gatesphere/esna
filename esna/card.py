#@+leo-ver=5-thin
#@+node:peckj.20140922102810.4053: * @file card.py
#@@language python

#@+<< imports >>
#@+node:peckj.20140922102810.4054: ** << imports >>
#@-<< imports >>
#@+<< declarations >>
#@+node:peckj.20140922102810.4055: ** << declarations >>
#@-<< declarations >>

#@+others
#@+node:peckj.20140922102810.4056: ** class Card
class Card:
  #@+others
  #@+node:peckj.20140922102810.4057: *3* __init__
  def __init__(self, levels, bs, gold, terrain, dungeon, events, reference, paths, monster, quest, hit):
    # these are lists
    self.levels = levels
    self.bs = bs
    self.gold = gold
    
    # these are scalars
    self.terrain = terrain
    self.dungeon = dungeon
    self.reference = reference
    self.paths = paths
    self.hit = hit
    
    # this is a dict tuple->string
    self.events = events
    
    # these are tuples (type, loot)
    self.monster = monster
    self.quest = quest
    

    
  #@+node:peckj.20140922102810.4058: *3* querying
  #@+node:peckj.20140922102810.4068: *4* get_monster_type
  def get_monster_type(self):
    return self.monster[0]
  #@+node:peckj.20140922102810.4070: *4* get_monster_loot
  def get_monster_loot(self):
    return self.monster[1]
  #@+node:peckj.20140922102810.4094: *4* get_quest_type
  def get_quest_type(self):
    return self.quest[0]
  #@+node:peckj.20140922102810.4096: *4* get_quest_loot
  def get_quest_loot(self):
    return self.quest[1]
  #@+node:peckj.20140922102810.4065: *4* get_bs
  def get_bs(self, index):
    return self.bs[index]
  #@+node:peckj.20140922102810.4067: *4* get_gold
  def get_gold(self, index):
    return self.gold[index]
  #@+node:peckj.20140922102810.4064: *4* get_level_index
  def get_level_index(self, level):
    return self.levels.index(level)
  #@+node:peckj.20140922102810.4063: *4* get_hit
  def get_hit(self):
    return self.hit
  #@+node:peckj.20140922102810.4062: *4* get_reference
  def get_reference(self):
    return self.reference
  #@+node:peckj.20140922102810.4059: *4* get_paths
  def get_paths(self):
    return self.paths
  #@+node:peckj.20140922102810.4060: *4* get_dungeon
  def get_dungeon(self):
    return self.dungeon
  #@+node:peckj.20140922102810.4061: *4* get_terrain
  def get_terrain(self):
    return self.terrain
  #@+node:peckj.20140924124512.4088: *4* get_events
  def get_events(self):
    return self.events
  #@-others
#@-others
#@-leo
