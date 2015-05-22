# Created using Python 3.4.1

import datetime

# strftime example
def to_string(my_datetime): # Turns a datetime into a string formatted date and time
  return my_datetime.strftime('%d %B %Y')

# strptime example
def from_string(my_date_string, my_format): # Turns a string into a formatted datetime
  return datetime.datetime.strptime(my_date_string, my_format)
