# Created using Python 3.4.1

from character import Character

class Warrior(Character):
  weapon = 'sword'
  
  def rage(self): # This ability will increase the attack limit of the warrior
    self.attack_limit = 20
    
  def __str__(self):
    return 'Warrior, {}, {}'.format(self.weapon, self.attack_limit)
