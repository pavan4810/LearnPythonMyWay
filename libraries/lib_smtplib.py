"""
Notes: =========================================================================
Notes: smtplib module:
Notes:
Notes:      smtplib.time
Notes:      smtplib.url2pathname
Notes:      smtplib.urlopen
Notes:      smtplib.urlparse
Notes:
"""

import smtplib

# Get to know about module smtplib content
print "========================================================================"
print "smtplib Module : start"
print dir(smtplib)
print "smtplib Module : end"
print "========================================================================"

server = smtplib.SMTP('localhost')
server.sendmail('pavan4810@gmail.com', 'pavan.avala@gmail.com',
    """To: pavan.avala@gmail.com
    From: pavan.avala@gmail.com
    
    Beware the Ides of March.
    """)
server.quit()
