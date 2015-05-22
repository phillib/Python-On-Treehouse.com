# Created using Python 3.4.1

# Write a function named time_machine that takes an integer 
# and a string of "minutes", "hours", "days", or "years". 
# This describes a timedelta. Return a datetime that is the 
# timedelta's duration from the starter datetime.

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)

def time_machine(num, unit):
  if unit in ("minutes", "hours", "days"):
    keyword = {unit : num} # Creates a dictionary with your number (num) and unit (unit).
  elif unit == "years":
    keyword = {"days" : num * 365} # Translates 'years' into 365 days.  
  return starter + datetime.timedelta(**keyword) # Unpacks your dictionary into your timedelta
