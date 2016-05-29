"""
Notes: =========================================================================
Notes: timeit module:
Notes:
Notes:      timeit.time
Notes:      timeit.timeit
Notes:      timeit.repeat
Notes:
"""

import timeit

# Get to know about module timeit content
print "========================================================================"
print "timeit Module : start"
print dir(timeit)
print "timeit Module : end"
print "========================================================================"

# Swapping numbers using temporary variable.
print timeit.Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

# Swapping numbers using tuple packing and unpacking.
print timeit.Timer('a,b = b,a', 'a=1; b=2').timeit()

#help(timeit.Timer)
