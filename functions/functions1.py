"""
Notes: =========================================================================
Notes: def function_name (arguments list):
Notes:     statement1
Notes:     ...
Notes:     statementN
Notes:     return x  # x can be single or multiple variables.
Notes:
"""

def doNothing():
   pass

doNothing()


def printSomething():
   print "Something"
   return 0

printSomething()


def sum(operand1, operand2):
   tmp = operand1 + operand2
   return tmp

print "Sum of %d and %d = %d" %(10, 11, sum(10,11))


def returnMultipleVariables(arg1, arg2, arg3):
  return arg1, arg2, arg3

print returnMultipleVariables(10, -20, 30)
