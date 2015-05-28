# Created using Python 3.4.1

# This program will take a meeting data and time and 
# convert it into a list of the 'OTHER_TIMEZONES'
# you MUST use 24 hour time for it to work properly.

from datetime import datetime

import pytz

OTHER_TIMEZONES = [
    pytz.timezone('US/Eastern'),
    pytz.timezone('Pacific/Auckland'),
    pytz.timezone('Asia/Calcutta'),
    pytz.timezone('UTC'),
    pytz.timezone('Europe/Paris'),
    pytz.timezone('Africa/Khartoum')
]
fmt = '%Y-%m-%d %H:%M:%S %Z%z'

while True:
    date_input = input("When is your meeting? Please use MM/DD/YYYY HH:MM format. ")
    try:
        local_date = datetime.strptime(date_input, '%m/%d/%Y %H:%M')
    except ValueError:
        print("{} doesn't seem to be a valid date & time.".format(date_input))
    else:  # else occurs when the user input is valid.
        local_date = pytz.timezone('US/Pacific').localize(local_date) # change local_date to match your local timezone
        utc_date = local_date.astimezone(pytz.utc) # convert to utc time
        
        output = [] # place to put your generated list of datetimes
        for timezone in OTHER_TIMEZONES:
            output.append(utc_date.astimezone(timezone))
        for appointment in output:
            print(appointment.strftime(fmt))
        break
