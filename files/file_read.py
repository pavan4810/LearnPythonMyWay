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
Notes: fd.read() reads entire file content
Notes:
Notes: fd.seek(offset[, whence]) adjusts files offset.
Notes:      whence 0: offset from start of file
Notes:      whence 1: relative to current position
Notes:      whence 2: offset from end
Notes:
Notes: fd.tell() current file position, an integer.
Notes:
Notes: fd.readline() reads one line
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

# reset file position offset
fd.seek(0)

# Read a line
print fd.readline()

# Close file.
fd.close()
