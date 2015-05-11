#Created using Python 3.4.1

shopping_list = []


def remove_item(idx):
  index = idx - 1
  item = shopping_list.pop(index)
  print("Remove {}.".format(item))


def show_help():
  print("\nSeparate each item with a comma.")
  print("Type DONE to quit, SHOW to see the current list, "
        "REMOVE to delete an item, and HELP to get this message.")
  
  
def show_list():
  count = 1
  for item in shopping_list:
    print("{}: {}".format(count, item))
    count += 1
    
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
