# Created using Python 3.4.1

import datetime

answer_format = '%m/%d' # the format you expect your user to enter
link_format = '%b_%d' # the format that wikipedia expects
link = 'https://en.wikipedia.org/wiki/{}' #wikipedia link except for month/year

while True:
  answer = input("What date would you like?  Please use the MM/DD format.  Enter 'quit' to quit. ")
  if answer.upper() == 'QUIT':
    break
    
  try: # makes a datetime using the user input (answer) and the answer format (answer_format)
    date = datetime.datetime.strptime(answer, answer_format) 
    output = link.format(date.strftime(link_format)) # appends correctly formatted date info to the wikipedia link
    print(output)
  except ValueError: # if user enters something other than a date in MM/DD format, throw an error.
    print("That's not a valid date.  Please try again. ")
  
