"""
Notes: =========================================================================
Notes: dir()
Notes:      The built-in function dir() is used to find out which names a module
Notes:      defines. It returns a sorted list of strings.
Notes:      It does not list the names of built-in functions and variables.
Notes:      They are defined in the standard module __builtin__.
Notes:      Ex: dir(), dir(modulename), dir(__builtin__)
Notes:
Notes: Four ways of importing modules (in the order of recommendation)
Notes:      1) from   module import printSomething
Notes:      2) import module as f
Notes:      3) import module
Notes:      4) from   module import *
Notes:
Notes: from module import *:
Notes:      This imports all names except those begining with an underscore(_)
Notes:
Notes: del module
Notes:
Notes: Module name is avaiable with .__name__.
Notes:      Ex: import module as f
Notes:          print f.__name__
Notes: 
Notes: Module name can be assigned to local variable
Notes:      Ex: fib = fibo.fib
Notes:          fib(500)
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
