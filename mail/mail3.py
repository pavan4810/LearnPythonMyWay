# Send mail with attachment

import smtplib
import base64

filename = "/tmp/test.txt"
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent) # base64

sender = 'pavala@cisco.com'
receivers = ['pavala@cisco.com']

marker = "AUNIQUEMARKER"
body ="""
This is a test email to send an attachement.
"""

# Define the main headers.
part1 = """From: Pavan Avala <pavala@cisco.com>
To: Pavan Avala <pavala@cisco.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit
%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s
%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
    smtpObj = smtplib.SMTP('mail.cisco.com', 25)
    smtpObj.sendmail(sender, receivers, message)
    print "Successfully sent email"
except SMTPException:
    print "Error: unable to send email"
