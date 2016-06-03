"""
Notes: =========================================================================
Notes: smtplib
Notes:      SMTP(host, port)
Notes:      sendmail(sender, receiver, message)
Notes:
"""

# Send message in Plain text format

import smtplib
sender = 'pavala@cisco.com'
receivers = ['pavala@cisco.com']

message = """From: Pavan Avala <paval@cisco.com>
To: Pavan Avala <pavala@cisco.com>
Subject: SMTP e-mail test
This is a test e-mail message.
Why there is no content inside mail.
"""

try:
    smtpObj = smtplib.SMTP('mail.cisco.com', 25)
    smtpObj.sendmail(sender, receivers, message)
    print "Successfully sent email"
except SMTPException:
    print "Error: unable to send email"
