#Created using Python 3.4.1

class Monster: #Make sure your class name is capitalized
  #hit_points = 1
  #color = 'yellow'  #Replaced by __init__ method below
  #weapon = 'sword'
  #sound = 'roar'
  
  def __init__(self, **kwargs):   #Doesn't return anything, just sets things
    self.hit_points = kwargs.get('hit_points', 1)
    self.weapon = kwargs.get('weapon', 'sword')
    self.color = kwargs.get('color', 'yellow')
    self.sound = kwargs.get('sound', 'roar')
  
  def battlecry(self):             #Every method you create on a class takes in the very least the 'self' argument.
    return self.sound.upper()      #'self' always represents the instance you are calling the method on.
                                   #You have to call the function on an instance of the class.
