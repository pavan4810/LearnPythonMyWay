"""
Notes: =========================================================================
Notes: fd.write(data) writes data into file
Notes:
Notes: fd.truncate(ToBytes) truncates the file
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

# Truncate the file.
fd.truncate(0)

fd.write(line1)
fd.write("\n")
fd.write(line2)
fd.write("\n")
fd.write(line3)
fd.write("\n")

# Close file.
fd.close()
