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
"""

from sys import argv

# Must provide exactly one argument
script, filename = argv

# Default mode is reading.
fd = open(filename)

# %r is used for generic purpose.
print "Here's is your file %r:" %(filename)

# Read and print file contents
print fd.read()

# Close file.
fd.close()
