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
  #@+node:peckj.20140922102810.4068: *4* getMonsterType
  def getMonsterType(self):
    return self.monster[0]
  #@+node:peckj.20140922102810.4070: *4* getMonsterLoot
  def getMonsterLoot(self):
    return self.monster[1]
  #@+node:peckj.20140922102810.4094: *4* getQuestType
  def getQuestType(self):
    return self.quest[0]
  #@+node:peckj.20140922102810.4096: *4* getQuestLoot
  def getQuestLoot(self):
    return self.quest[1]
  #@+node:peckj.20140922102810.4065: *4* getBS
  def getBS(self, index):
    return self.bs[index]
  #@+node:peckj.20140922102810.4067: *4* getGold
  def getGold(self, index):
    return self.Gold[index]
  #@+node:peckj.20140922102810.4064: *4* getLevelIndex
  def getLevelIndex(self, level):
    return self.levels.index(level)
  #@+node:peckj.20140922102810.4063: *4* getHit
  def getHit(self):
    return self.hit
  #@+node:peckj.20140922102810.4062: *4* getReference
  def getReference(self):
    return self.reference
  #@+node:peckj.20140922102810.4059: *4* getPaths
  def getPaths(self):
    return self.paths
  #@+node:peckj.20140922102810.4060: *4* getDungeon
  def getDungeon(self):
    return self.dungeon
  #@+node:peckj.20140922102810.4061: *4* getTerrain
  def getTerrain(self):
    return self.terrain
  #@-others
#@-others
#@-leo
