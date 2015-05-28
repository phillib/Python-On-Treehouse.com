# Created using Python 3.4.1

import datetime

import pytz

starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(timezone_name):
  """
  This function takes a timezone as a user input
  and converts the starter time to that timezone
  """
  new_timezone = pytz.timezone(timezone_name)
  return starter.astimezone(new_timezone)
