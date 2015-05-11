# This code utilizes Python 3.4.1

shopping_list = [] #Creates an empty list to start with.


def show_help(): #Function to show help.
  print("\nSeparate each item with a comma.")
  print("Type DONE to quit, SHOW to see the current list, and HELP to get this message.")
  
  
def show_list(): #Function to show your list (example: 1: Cheese, 2: Pretzels)
  count = 1
  for item in shopping_list:
    print("{}: {}".format(count, item))
    count += 1
    
print("Give me a list of things you want to shop for.")
show_help()

while True:
  new_stuff = input("> ")
  
  if new_stuff == "DONE":
    print("\nHere's your list:")
    show_list()
    break
  elif new_stuff == "HELP":
    show_help()
    continue
  elif new_stuff == "SHOW":
    show_list()
    continue
  else:
    new_list = new_stuff.split(",")
    index = input("Add this at a certain spot? Press enter for the end of the list, "
                  "or give me a number.  Currently {} items in the list. > ".format(
        len(shopping_list)))
    if index:
      try:
        spot = int(index) - 1 #spot subtracts 1 because the count on line 12 starts with 1, not 0 (python indexing starts at 0)
      except:
        print("Oops!  Looks like you didn't enter a list number for where to enter your items.")
        continue
      for item in new_list:
        shopping_list.insert(spot, item.strip()) #item.strip() takes any white space out from the items entered
        spot += 1
    else:
      for item in new_list:
        shopping_list.append(item.strip()) #inserts items at the end of your list
