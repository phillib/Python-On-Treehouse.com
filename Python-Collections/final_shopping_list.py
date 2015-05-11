#Created using Python 3.4.1

shopping_list = []


def remove_item(idx):
  index = idx - 1
  item = shopping_list.pop(index)
  print("Remove {}.".format(item))


def show_help():
  print("\nSeparate each item with a comma.")
  print("Type DONE to quit, SHOW to see the current list, "
        "REMOVE to delete an item, MOVE to move an item, "
        "CLEAR to empty your list, and HELP to get this message.")
  
  
def show_list():
  count = 1
  for item in shopping_list:
    print("{}: {}".format(count, item))
    count += 1
  if shopping_list == []:
    print("Your shopping list is currently empty")
    
    
def move_item(to_move, new_position): #Moves an item currently in your list to a new position of your choosing.
  index = to_move - 1
  position = new_position - 1
  shopping_list.insert(position, shopping_list.pop(index))
  
  
def clear_list(): #This targets the global variable for shopping_list and empties its contents
  global shopping_list
  shopping_list = []
  
    
print("Give me a list of things you want to shop for.")
show_help()

while True:
  new_stuff = input("> ")
  
  if new_stuff.lower() == "done":
    print("\nHere's your list:")
    show_list()
    break
  elif new_stuff.lower() == "help":
    show_help()
    continue
  elif new_stuff.lower() == "show":
    show_list()
    continue
  elif new_stuff.lower() == "remove":
    show_list()
    idx = input("Which item?  Tell me the number. ")
    remove_item(int(idx))
    continue
  elif new_stuff.lower() == "move":
    show_list()
    to_move = input("Which item number would you like to move? ")
    new_position = input("Great!  Now where on the list would you like to move it? ")
    move_item(int(to_move), int(new_position))
    continue
  elif new_stuff.lower() == "clear":
    show_list()
    answer = input("Are you sure you want to clear the current list? (Y/N) ")
    if answer.lower() == "y":
      clear_list()
      print("Your shopping list is now empty.")
      continue
    elif answer.lower() == "n":
      print("Your shopping list is unchanged.")
      continue
    else:
      print("Please enter 'Y' or 'N' as your selection.  Type 'CLEAR' to try again")
      continue
  else:
    new_list = new_stuff.split(",")
    index = input("Add this at a certain spot? Press enter for the end of the list, "
                  "or give me a number.  Currently {} items in the list. > ".format(
        len(shopping_list)))
    if index:
      try:
        spot = int(index) - 1
      except:
        print("Oops!  Looks like you didn't enter a list number for where to enter your items.")
        continue
      for item in new_list:
        shopping_list.insert(spot, item.strip())
        spot += 1
    else:
      for item in new_list:
        shopping_list.append(item.strip())
