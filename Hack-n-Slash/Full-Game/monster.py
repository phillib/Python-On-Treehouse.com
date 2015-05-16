# Created using Python 3.4.1

import random

from combat import Combat

COLORS = ['yellow', 'red', 'blue', 'green']

class Monster(Combat): #Make sure your class name is capitalized
  min_hit_points = 1
  max_hit_points = 1
  min_experience = 1
  max_experience = 1
  weapon = 'sword'
  sound = 'roar'
  
  def __init__(self, **kwargs):   #Doesn't return anything, just sets things
    self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
    self.experience = random.randint(self.min_experience, self.max_experience)
    self.color = random.choice(COLORS)
    
    for key, value in kwargs.items(): #allows you to set attributes other than those listed above
      setattr(self, key, value) #setattr takes three arguments:  object, attribute to set, value
      
  def __str__(self): # Called whenever something is converted to a string (such as printing one of your monsters)
    return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                          self.__class__.__name__, #__class__(e.g., goblin or troll).__name__(string
                                          self.hit_points,                    # version of your class)
                                          self.experience)
      
  def battlecry(self):             #Every method you create on a class takes in the very least the 'self' argument
    return self.sound.upper()      #'self' always represents the instance you are calling the method on.
                                   #You have to call the function on an instance of the class.
    
    
#Below are examples of inheritance.  Goblin, for instance, is a sublcass of Monster and
#Inherits all of the attributes of Monster unless otherwise specified.
    
class Goblin(Monster): #Having Monster in the parenthesis makes Goblin a subclass of Monster
  max_hit_points = 3
  max_experience = 2
  sound = 'squeak'
  
  
class Troll(Monster):
  min_hit_points = 3
  max_hit_points = 5
  min_experience = 2
  max_experience = 6
  sound = 'growl'
  

class Dragon(Monster):
  min_hit_points = 5
  max_hit_points = 10
  min_experience = 6
  max_experience = 10
  sound = 'raaaaaar'
