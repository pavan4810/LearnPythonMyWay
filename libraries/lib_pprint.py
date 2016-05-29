"""
Notes: =========================================================================
Notes: pprint module:
Notes:
Notes:
"""

import pprint

# Get to know about module pprint content
print "========================================================================"
print "pprint Module : start"
print dir(pprint)
print "pprint Module : end"
print "========================================================================"

t = (((('black', 'cyan'), 'white', ('green', 'red')), (('magenta', 'yellow'), 'blue')))
pprint.pprint(t, width=30)

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=30)
