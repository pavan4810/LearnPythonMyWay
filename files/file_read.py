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
Notes: Following for loop also reads file content
Notes: for line in fd:
Notes     print line
Notes:
Notes: "print fd" prints info about file descriptor.
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
Notes: exists(filename) to check whether file exists or not
"""

from sys import argv
from os.path import exists


#===============================================================================
# Must provide exactly one argument
script, filename = argv

# Check whether file exists
print "Does the input file exist? %r" % exists(filename)


#===============================================================================
# Default mode is reading.
fd = open(filename)

# Print info about file descriptor
print "Info about file descriptor : ", fd


#===============================================================================
# %r is used for generic purpose.
print "Here's is your file %r:" %(filename)



#===============================================================================
# Read and print file contents
print "One way to read file is fd.read()\n", fd.read()

fd.seek(0)

# Read file content using for loop
print "Another way to read file is for loop\n"
for line in fd:
  print line,


#===============================================================================
# reset file position offset
fd.seek(0)


#===============================================================================
# Read a line
print "Reading single line from file"
print fd.readline()


#===============================================================================
# Close file.
fd.close()
