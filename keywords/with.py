"""
Notes: =========================================================================
Notes: with open(filename) as fd:
Notes:      file operations
Notes:
Notes: Using "with" has advantage that the file is properly closed after its
Notes: suite finishes, even if an exception is raised on the way. It is also
Notes: much shorter than writing equivalent try-finally.
Notes:
"""

from sys import argv
from os.path import exists

#===============================================================================
# Must provide exactly one argument
script, filename = argv

# Check whether file exists
print "Does the input file exist? %r" % exists(filename)

#===============================================================================
with open(filename) as fd:
    print "Info about file descriptor : ", fd
    print fd.read()

print "Info about file descriptor : ", fd
