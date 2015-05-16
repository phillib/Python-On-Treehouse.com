# Created using Python 3.4.1

import random

from combat import Combat


class Character(Combat):
  attack_limit = 10
  experience = 0
  base_hit_points = 10 # Your character starting hit points is 10
  
  def attack(self): # This will override inheritance from combat.py
    roll = random.randint(1, self.attack_limit)
    if self.weapon == 'sword':
      roll += 1
    elif self.weapon == 'axe':
      roll += 2
    return roll > 4 # You get a hit on any number from 5 to 10
  
  
  def get_weapon(self): #This function will limit what weapons user can choose.
    weapon_choice = input("Weapon ([S]word, [A]xe, [B]ow: ").lower() #User chooses weapon
    
    if weapon_choice in 'sab': #'sab' corresponds to first letters for weapons above.
      if weapon_choice == 's':
        return 'sword'
      elif weapon_choice == 'a':
        return 'axe'
      else:
        return 'bow'
    else:
      return self.get_weapon()
    
  
  def __init__(self, **kwargs):
    self.name = input("Name: ") #Allow user to choose their name.
    self.weapon = self.get_weapon() #Prompts user to choose weapon using above function.
    self.hit_points = self.base_hit_points # Starting hit points
    
    for key, value in kwargs.items():
      setattr(self, key, value)
      
  def __str__(self): # Will determine what prints when you print character (self.player)
    return '{}, HP: {}, XP: {}'.format(self.name, self.hit_points, self.experience)
  
  def rest(self): # When your character rest, you gain 1 hit point back.
    if self.hit_points < self.base_hit_points:
      self.hit_points += 1
      
  def leveled_up(self): # level up if you get 5 experience or more
    return self.experience >= 5
