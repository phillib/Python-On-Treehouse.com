# Created using Python 3.4.1

import datetime

def time_tango(my_date, my_time):
  """
  This function takes a date and a time
  and combines them for you.
  """
  my_tango = datetime.datetime.combine(my_date, my_time)
  return my_tango
