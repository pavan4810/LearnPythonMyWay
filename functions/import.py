"""
Notes: =========================================================================
Notes: Four ways of importing modules (in the order of recommendation)
Notes:      1) from   functions1 import printSomething
Notes:      2) import functions1 as f
Notes:      3) import functions1
Notes:      4) from   functions1 import *
Notes:
Notes: del module
Notes:
"""

print "========================================================================"
print "Before importing a module\n", dir()
from functions import printSomething
print "After  importing a module\n", dir()

printSomething()

del printSomething
print "After  unloading a module\n", dir()
print "========================================================================"



print "========================================================================"
print "Before importing a module\n", dir()
import functions as f
print "After  importing a module\n", dir()

f.printSomething()

del f
print "After  unloading a module\n", dir()
print "========================================================================"



print "========================================================================"
print "Before importing a module\n", dir()
import functions
print "After  importing a module\n", dir()

functions.printSomething()

del functions
print "After  unloading a module\n", dir()
print "========================================================================"



print "========================================================================"
print "Before importing a module\n", dir()
from functions import *
print "After  importing a module\n", dir()

printSomething()

del printSomething
del doNothing
del returnMultipleVariables
del sum
print "After  unloading a module\n", dir()
print "========================================================================"
