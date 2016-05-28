"""
Notes: =========================================================================
Notes: glob module:
Notes:  The glob module provides a function for making file lists from directory
Notes:  wildcard searches.
Notes:
Notes:      glob.glob()
Notes:
"""

import glob

# Get to know about module glob content
print "========================================================================"
print "Glob Module : start"
print dir(glob)
print "Glob Module : end"
print "========================================================================"

for file in glob.glob("*.py"):
    print "File: ", file

for file in glob.glob("*.py"):
    print "File: ", file
