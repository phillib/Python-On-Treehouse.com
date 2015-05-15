#Created using Python 3.4.1

import random

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]


def get_locations():
  # monster = random
  monster = random.choice(CELLS)
  # door = random
  door = random.choice(CELLS)
  # start = random
  start = random.choice(CELLS
  
  # if monster, door, or start are the same, do it again
  if monster == door or monster == start or door == start:
    return get_locations()
  # return monster, door, start
  return monster, door, start
  
  
def move_player(player, move):
  # Get the player's current location
  # If move is LEFT, y - 1
  # If move is RIGHT, y + 1
  # If move is UP, x - 1
  # If move is DOWN, x + 1
  return player


def get_moves(player):
  moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
  # player = (x, y)
                        
  if player[1] == 0:
  # if player's y is 0, remove LEFT
    moves.remove('LEFT')
  if player[0] == 0:
  # if player's x is 0, remove UP
    moves.remove('UP')
  if player[1] == 2:
  # if player's y is 2, remove RIGHT
    moves.remove('RIGHT')
  if player[0] == 2:                     
  # if player's x is 2, remove DOWN
    moves.remove('DOWN')
  return moves
                        
monster, door, player = get_locations()                        
                        

while True:
  moves = get_moves(player)
                        
  print("Welcome to the dungeon!")
  print("You're currently in room {}".format(player))  # fill in with player position
  print("You can move {}".format(moves))  # fill in with available moves
  print("Enter QUIT to quit")
  
  move = input("> ")
  move = move.upper()
  
  if move == 'QUIT':
    break
                        
  if move in moves: # If it's a good move, change the player's position
    player = move_player(player, move)
  else: # If it's a bad move, don't change anything
    print("** Walls are hard, stop walking into them! **")
    continue
    
  if player == door: # If the new player position is the door, they win!
    print("You escaped!")
    break
  elif player == monster: # If the new player position is the monster, they lose!
    print("You were eaten by the grue!")
    break
  
  
  
