# Created using Python 3.4.1

# Must first install pytz using 'pip install pytz'
# For formatting 'fmt' see 'strftime.org'

import datetime
import pytz

pacific = pytz.timezone('US/Pacific')
eastern = pytz.timezone('US/Eastern')

fmt = '%Y-%m-%d %H:%M:%S %Z%z' # %Z%z will show your localized time (PDT-0700)

utc = pytz.utc # will convert your time into utc time

# localize takes a date time and gives it to you with a certain time zone
start = pacific.localize(datetime.datetime(2015, 5, 23, 9)) 
print(start.strftime(fmt))

start_eastern = start.astimezone(eastern)
print(start_eastern)

start_utc = datetime.datetime(2015, 5, 23, 1, tzinfo=utc)
print(start_utc.strftime(fmt))

start_pacific = start_utc.astimezone(pacific)
print(start_pacific)

#### convert a timezone to any in the world below:
# As long as you start with a UTC time you can easily generate
# corresponding dates and times for anywhere in the world

## Also try implementing the 'delorean' package below
## to simplify the process

auckland = pytz.timezone('Pacific/Auckland')
mumbai = pytz.timezone('Asia/Calcutta')
apollo_13_naive = datetime.datetime(1970, 4, 11, 14, 13) # step 1

apollo_13_eastern = eastern.localize(apollo_13_naive) # step 2
print(apollo_13_eastern)

apollo_13_utc = apollo_13_eastern.astimezone(utc) # step 3

print(apollo_13_utc.astimezone(pacific).strftime(fmt)) # easily convert to pacific time

print(apollo_13_utc.astimezone(auckland).strftime(fmt)) # easily convert to auckland time

print(apollo_13_utc.astimezone(mumbai).strftime(fmt)) # easily convert to mumbai time

### If you do not know your timezones, the following will print them all 
### for you in the console: pytz.all_timezones

### If you just want country timezones, the following will print them
### given the two letter country code:  pytz.country_timezones['us']

### For more on converting datetimes, see the following link:
### http://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/

### Additional libraries related to time:  
### Delorean: http://delorean.readthedocs.org/en/latest/  
### Chronyk: https://pypi.python.org/pypi/Chronyk/0.9.1
