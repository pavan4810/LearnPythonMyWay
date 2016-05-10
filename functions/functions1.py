"""
Notes: =========================================================================
Notes: def function_name (arguments list):
Notes:      statement1
Notes:      ...
Notes:      statementN
Notes:      return x  # x can be single or multiple variables.
Notes:
Notes: def function_name (arg1, arg2=default_value, arg3=default_value)
Notes:      statements
Notes:      return x  # x can be single or multiple variables.
Notes:
Notes:      The default values are evaluated at the point of function definition
Notes:      in the defining scope
Notes:      The default value is evaluated only once. This makes a difference
Notes:      when the default is a mutable object such as a list, dictionary, or
Notes:      instances of most classes.
Notes:
"""

#===============================================================================
def doNothing():
   pass

doNothing()


#===============================================================================
def printSomething():
   print "Something"
   return 0

printSomething()


#===============================================================================
def sum(operand1, operand2):
   tmp = operand1 + operand2
   return tmp

print "Sum of %d and %d = %d" %(10, 11, sum(10,11))


#===============================================================================
def returnMultipleVariables(arg1, arg2, arg3):
  return arg1, arg2, arg3

print returnMultipleVariables(10, -20, 30)


#===============================================================================
def ask_ok(prompt, retries=4, complaint='Yes or No, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes', 'Yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope', 'No'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

# With mandatory arguments
ask_ok('Do you really want to quit?')

# With mandatory arguments + 1 optioinal argument
ask_ok('OK to overwrite the file?', 2)

# With all arguments
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


#===============================================================================
i = 5
def f(arg=i):
    print arg

i = 6
# f() return 5, not 6
f()


#===============================================================================
def f1(a, L=[]):
    L.append(a)
    return L

print f1(1)
print f1(2)
print f1(3)

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print f2(1)
print f2(2)
print f2(3)
