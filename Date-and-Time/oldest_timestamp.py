# Create a function named timestamp_oldest that takes any number 
# of POSIX timestamp arguments. Return the oldest one as a datetime object.

# If you need help, look up datetime.datetime.fromtimestamp()
# Also, remember that you *will not* know how many timestamps
# are coming in.

import datetime

def timestamp_oldest(*args):
    timestamps = list(args)
    timestamps.sort() 
    conversion = datetime.datetime.fromtimestamp(timestamps[0]) #<-- "oldest" is lowest number
    return conversion
