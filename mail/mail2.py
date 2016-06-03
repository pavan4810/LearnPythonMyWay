# Send message in HTML format

import smtplib
import smtplib
sender = 'pavala@cisco.com'
receivers = ['pavala@cisco.com']

message = """From: Pavan Avala <paval@cisco.com>
To: Pavan Avala <pavala@cisco.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test
This is an e-mail message to be sent in HTML format
<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
    smtpObj = smtplib.SMTP('mail.cisco.com', 25)
    smtpObj.sendmail(sender, receivers, message)
    print "Successfully sent email"
except SMTPException:
    print "Error: unable to send email"
