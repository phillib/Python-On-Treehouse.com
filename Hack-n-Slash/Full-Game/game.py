# Creates using Python 3.4.1

import sys

from character import Character # 1. Import your character and your monsters.
from monster import Dragon      #    No need to import combat.py because it
from monster import Goblin      #    is imported into character.py and monster.py
from monster import Troll


class Game:
  def setup(self): # setup will allow game to run at start each time
    self.player = Character() # Will set up player and prompt for name and weapon
    self.monsters = [ # Total monsters 
      Goblin(),
      Troll(),
      Dragon()
      ]
    self.monster = self.get_next_monster() # Monster currently being battled.
    
  def get_next_monster(self):
    try:
      return self.monsters.pop(0) # Will pull out the first monster in your list to battle.
    except IndexError:
      return None # If no monsters remain, no monster will be returned.
    
    
  def monster_turn(self): # What happens when the monster attacks on its turn.
    # Check to see if the monster attacks
    if self.monster.attack():
      # If so, tell the player
      print("{} is attacking!".format(self.monster))
      # Check if the player wants to dodge
      if input("Dodge? Y/N ").lower() == 'y':
        # If so, see if the dodge is successful
        if self.player.dodge():
          # If it is, move on
          print("You dodged the attack!")
        else:
          # If it's not, remove one player hit point
          print("You got hit anyway!")
          self.player.hit_points -= 1
      else:
        print("{} hit you for 1 point!".format(self.monster))
        self.player.hit_points -= 1     
    # If the monster isn't attacking, tell that to the player too.
    else:
      print("{} isn't attacking this turn.".format(self.monster))
    
    
  def player_turn(self):
    # Let the player attack, rest, or quit
    player_choice = (input("[A]ttack, [R]est, [Q]uit? ").lower())
    # If they attack:
    if player_choice == 'a':
      print("You're attacking {}!".format(self.monster))
      # See if the attack is successful
      if self.player.attack():
        # If so, see if the monster dodges
        if self.monster.dodge():
          # If dodged, print that
          print("{} dodged your attack!".format(self.monster))
        # If not dodged, subtract the right num of hit points from the monster
        else:
          if self.player.leveled_up():
            self.monster.hit_points -= 2
          else:
            self.monster.hit_points -= 1
          print("You hit {} with your {}!".format(
                self.monster, self.player.weapon))
      # If not a good attack, tell the player
      else:
        print("You missed!")
    # If they rest:            
    elif player_choice == 'r':
      # Call the player.rest() method          
      self.player.rest()
    # If they quit, exit the game
    elif player_choice == 'q':
      sys.exit() # will exit the program
    # If they pick anything else, re-run this method
    else:
      self.player_turn()
                
  def cleanup(self): # What to do when you beat a monster
    # If the monster has no more hit points:
    if self.monster.hit_points <= 0:
      # up the player's experience
      self.player.experience += self.monster.experience
      # print a message
      print("You killed {}!".format(self.monster))
      # Get a new monster
      self.monster = self.get_next_monster()
      
  def __init__(self):
    self.setup()
    
    # While player still has hit points and there are monsters remaining
    while self.player.hit_points and (self.monster or self.monsters):
      print('\n'+'='*20) # adds a spacer such as: ===========
      print(self.player) # Determined by __str__ method in character.py
      self.monster_turn()
      print('-'*20) # A nice seperator between player and monster turn
      self.player_turn()
      self.cleanup() # Move to this if you beat a monster
      print('\n'+'='*20)
    
    # If you exit the above while loop and your player still has hit points,
    # You win!
    if self.player.hit_points: # hit_points comes from __init__ in character.py
      print("You win!")
    # If you exit the above while loop and there are monsters remaining, but
    # you are out of hit points, you lose...
    elif self.monsters or self.monster:
      print("You lose!")
    sys.exit() # Once the game is over, win or lose, exit the game.
                
Game() # starts the game when you enter 'python game.py'
      
