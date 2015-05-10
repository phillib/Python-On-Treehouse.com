#Created using Python 3

shopping_list = list() #Empty list

print("What should we pick up at the store?") #Instructions
print("Enter 'DONE' to stop adding items.") #Instructions continued

while True: #While loop for list input
  new_item = input("> ") #Creates user input prompt
  
  if new_item == 'DONE': #If user enters 'DONE', the list completes and exits the loop
    break
    
  shopping_list.append(new_item) #The item entered by the user is appended to the list
  print("Added! List has {} items.".format(len(shopping_list))) 
  continue #continues prompting user for more shopping list items
  
print("Here's your list:")

for item in shopping_list: #prints all items in your new list
  print(item)
