"""
Notes: =========================================================================
Notes: sys module:
Notes:
Notes:      sys.argv
Notes:
Notes:      sys.modules
Notes:      sys.path
Notes:
Notes:      sys.stdin
Notes:      sys.stdout
Notes:      sys.stderr
Notes:
"""

import sys

# Get to know about module sys content
print "========================================================================"
print "Sys Module : start"
print dir(sys)
print "Sys Module : end"
print "========================================================================"

for arg in sys.argv:
    print "Args: ", arg

print "\n\nPrinting error log using sys.stderr.write()"
sys.stderr.write('Warning, log file not found starting a new one.\n')

print "\n\nPython Path :\n", sys.path
print "\n\nPython Modules :\n", sys.modules
