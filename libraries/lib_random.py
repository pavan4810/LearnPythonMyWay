"""
Notes: =========================================================================
Notes: random module:
Notes:
Notes:      random.choice
Notes:      random.division
Notes:      random.getstate
Notes:      random.randint
Notes:      random.random
Notes:      random.randrange
Notes:      random.sample
Notes:      random.seed
Notes:
"""

import random

# Get to know about module random content
print "========================================================================"
print "Random Module : start"
print dir(random)
print "Random Module : end"
print "========================================================================"

print random.choice(['apple', 'mango', 'banana'])

print random.sample(xrange(10), 10)    # sampling without replacement

print random.random()                   # random float

print random.randrange(6)               # random integer chosen from range(6)
