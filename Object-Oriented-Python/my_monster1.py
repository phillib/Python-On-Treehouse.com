# Created using Python 3.4.1

import random

COLORS = ['yellow', 'red', 'blue', 'green']

class Monster: #Make sure your class name is capitalized
  min_hit_points = 1
  max_hit_points = 1
  min_experience = 1
  max_experience = 1
  weapon = 'sword'
  sound = 'roar'
  
  def __init__(self, **kwargs):   #Doesn't return anything, just sets things initially if not specified.
    self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
    self.experience = random.randint(self.min_experience, self.max_experience)
    self.color = random.choice(COLORS)
    
    for key, value in kwargs.items(): #allows you to set attributes other than those listed above
      setattr(self, key, value) #setattr takes three arguments:  object, attribute to set, value
      
  def battlecry(self):             #Every method you create on a class takes in the very least the 'self' argument.
    return self.sound.upper()      #'self' always represents the instance you are calling the method on.
                                   #You have to call the function on an instance of the class.
