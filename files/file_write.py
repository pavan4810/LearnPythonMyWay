"""
Notes: =========================================================================
Notes: open(filename [, mode [,buffering]])
Notes:   This function opens specified file for file operations.
Notes:   mode:
Notes:      "r"-reading (default),
Notes:       "w"-writing,
Notes:       "a"-appending
Notes:       append "+" to mode for simultanous read and write.
Notes:   Buffering: If the buffering argument is given,
Notes:      0 means unbuffered,
Notes:      1 means line buffered, and
Notes:      larger numbers specify the buffer size.
Notes:  
Notes:
"""

from sys import argv

# Must provide exactly one argument
script, filename = argv

# Open file for writing
fd = open(filename, 'w')

# Read lines from stdin
print "Now I'm going to ask you for three lines."
line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

# Write to file. Need to add new line character
fd.write(line1)
fd.write("\n")
fd.write(line2)
fd.write("\n")
fd.write(line3)
fd.write("\n")

# Close file.
fd.close()
