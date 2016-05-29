"""
Notes: =========================================================================
Notes: urllib2 module:
Notes:
Notes:      urllib2.time
Notes:      urllib2.url2pathname
Notes:      urllib2.urlopen
Notes:      urllib2.urlparse
Notes:
"""

import urllib2

# Get to know about module urllib2 content
print "========================================================================"
print "Urllib2 Module : start"
print dir(urllib2)
print "Urllib2 Module : end"
print "========================================================================"

import urllib2
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print line
