"""
Notes: =========================================================================
Notes: datetime module:
Notes:
Notes:      datetime.date
Notes:      datetime.datetime
Notes:      datetime.time
Notes:      datetime.timedelta
Notes:      datetime.tzinfo
Notes:
"""

import datetime

# Get to know about module datetime content
print "========================================================================"
print "datetime Module : start"
print dir(datetime)
print "datetime Module : end"
print "========================================================================"

now = datetime.date.today()
print now
print now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

# dates support calendar arithmetic
birthday = datetime.date(1984, 5, 25)
age = now - birthday
print age
print age.days

#help(datetime.date)
