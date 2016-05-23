"""
Notes: =========================================================================
Notes:  Different ways of handling exceptions.
Notes:      try:
Notes:          statement
Notes:          raise Exception(args)
Notes:      except EXCEPTIONTYPE1:
Notes:          handling
Notes:      except EXCEPTIONTYPE1 as variable:
Notes:          print type(variable)
Notes:          print "So and so", variable.methods
Notes:          handling
Notes:      except (ET1, ET2, ET3, ...):
Notes:          handling
Notes:      except:
Notes:          handling
Notes:          raise
Notes:      else:
Notes:          If no exception, process statements here
Notes:      finally:
Notes:          Irrespective of exception, process statements here
Notes: 
Notes:  raise Exception(arguments)
Notes:      An argument to raise indicates the exception to be raised.
Notes:      That must be either an exception instance or
Notes:      an exception class (a class that derives from Exception).
Notes: 
Notes:  sys.exc_info()[0] gives unexpected error type
Notes: 
Notes:  User Defined exceptions. 
Notes:      class MyError(Exception):
Notes:          def __init__(self, value):
Notes:              self.value = value
Notes:          def __str__(self):
Notes:              return repr(self.value)
Notes: 
Notes: 
"""

while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."
    except (RuntimeError, TypeError, NameError):
        pass



#===============================================================================
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print type(inst)     # the exception instance
    print inst.args      # arguments stored in .args
    print inst           # __str__ allows args to be printed directly
    x, y = inst.args
    print 'x =', x
    print 'y =', y



#===============================================================================
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise



#===============================================================================
class MyError(Exception):               # Inheriting from Exception class
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print 'My exception occurred, value:', e.value
    print 'My exception occurred, value:', e.__str__()
