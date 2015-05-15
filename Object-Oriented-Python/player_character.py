# Created using Python 3.4.1

class Character:
  experience = 0
  hit_points = 10
  
  
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
    
    for key, value in kwargs.items():
      setattr(self, key, value) # Allows you to assign new attributes to your character
