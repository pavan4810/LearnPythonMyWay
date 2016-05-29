"""
Notes: =========================================================================
Notes: time module:
Notes:
Notes:      time.time
Notes:      time.localtime
Notes:      time.gmtime
Notes:      time.asctime
Notes:      time.clock
Notes:      time.sleep
Notes:      time.mktime
Notes:      time.strftime
Notes:      time.strptime
Notes:
"""

import time

# Get to know about module time content
print "========================================================================"
print "time Module : start"
print dir(time)
print "time Module : end"
print "========================================================================"

# Number of ticks
ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks


# Local time. Converts ticks to tuple.
# time.mktime() Converts tuple to ticks.
localtime = time.localtime(time.time())
print "Local current time :", localtime
print "Year               :", localtime.tm_year
print "Month              :", localtime.tm_mon
print "Day of the month   :", localtime.tm_mday
print "Hours              :", localtime.tm_hour
print "Minutes            :", localtime.tm_min
print "Seconds            :", localtime.tm_sec
print "Day of the week    :", localtime.tm_wday
print "Day of the year    :", localtime.tm_yday
print "Is DST             :", localtime.tm_isdst


# Local time in ASCII format.
localtime = time.asctime( time.localtime(time.time()) )
print "LTime in ASCII fmt :", localtime


# Global time in ASCII format.
globaltime = time.asctime( time.gmtime(time.time()) )
print "GTime in ASCII fmt :", globaltime 


# Ctime
localtime = time.ctime(time.time())
print "LTime in c fmt     :", localtime


# Time using CPU Clock. Used to measure performance.
#t0 = time.clock()
# Execute code
#t1 = time.clock()
#print "Code took :", t1-t0 
print "CPU Clock          :", time.clock()


# Take tuple as input and print time is specified format
t = (2016, 5, 29, 12, 44, 38, 0, 0, 0)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.localtime(t))
#===============================================================================
import calendar

# Get to know about module time content
print "========================================================================"
print "calendar Module : start"
print dir(calendar)
print "calendarModule : end"
print "========================================================================"


# Get month calendar
cal = calendar.month(2016, 5)
print "calendar           :\n", cal


# Leap year calculator
print "Is year 2016 a leap year ?:", calendar.isleap(2016)
