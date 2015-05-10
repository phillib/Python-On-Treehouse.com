#This code utilizes Python 3.4.1

import random

print("Welcome to guess the number!  Guess the random number between 1 and 10!")
print("You have 3 guesses to guess correctly.  Good luck!")

answer = random.randint(1, 10)

guesses_remaining = 3
guesses_made = 0

while True:

  guess = input("Enter your guess: ")
  
  try: #This block of code(lines 17-21) checks to ensure that the user is entering a whole number
    player_num = int(guess)
  except:
    print("That's not a whole number!  Enter a whole number.")
    continue
    
  if not player_num > 0 or not player_num < 11: #This block of code ensures that the users guess is between 1 and 10
    print("That number isn't between 1 and 10.")
    continue
  
  if guesses_remaining < 2: #Once the user runs out of guesses, the game exits
    print("Sorry, you ran out of guesses.  Thanks for playing!")
    break
  
  if player_num < answer:
    print("Sorry, your guess it too LOW.  Try again!")
    guesses_made = guesses_made + 1
    guesses_remaining = guesses_remaining - 1
    print("You have guessed {} times.".format(guesses_made))
    continue
  elif player_num > answer:
    print("Sorry, your guess is too HIGH.  Try again!")
    guesses_made = guesses_made + 1
    guesses_remaining = guesses_remaining - 1
    print("You have guessed {} times.".format(guesses_made))
    continue
  else:
    print("Correct!  You WIN!!!")
    break
