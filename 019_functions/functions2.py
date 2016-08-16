"""
Notes: =========================================================================
Notes: Different ways of argument passing.
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
Notes: def parrot(voltage, state='a stiff', action='voom', type='Indian Blue'):
Notes:      print "-- This parrot wouldn't", action,
Notes:      print "if you put", voltage, "volts through it."
Notes:      print "-- Lovely plumage, the", type
Notes:      print "-- It's", state, "!"
Notes: 
Notes: This function can be called in following ways
Notes:      parrot(1000)                               # 1 positional argument
Notes:      parrot(voltage=1000)                       # 1 keyword argument
Notes:      parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
Notes:      parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
Notes:      parrot('a million', 'life', 'jump')        # 3 positional arguments
Notes:      parrot('a thousand', state='pushing up')   # 1 positional, 1 keyword
Notes: 
"""

#===============================================================================
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
      print "-- This parrot wouldn't", action,
      print "if you put", voltage, "volts through it."
      print "-- Lovely plumage, the", type
      print "-- It's", state, "!\n"

print ""
print "def parrot(voltage, state='a stiff', action='voom', type='Blue'):"
print ""
print "Following succeeds"
print "#======================================================================="
print "parrot(1000)                                 " # 1 positional argument
print "parrot(voltage=1000)                         " # 1 keyword argument
print "parrot(voltage=1000000, action='VOOOOOM')    " # 2 keyword arguments
print "parrot(action='VOOOOOM', voltage=1000000)    " # 2 keyword arguments
print "parrot('a million', 'bereft of life', 'jump')" # 3 positional arguments
print "parrot('a thousand', state='pushing up')     " # 1 positional, 1 keyword



#===============================================================================
print ""
print "Following fails"
print "#======================================================================="
print "parrot()                     "
print "parrot(voltage=5.0, 'dead')  "
print "parrot(110, voltage=220)     "
print "parrot(actor='John Cleese')  "
print "parrot(action='VOOOOOM', 1000000)  "
print "parrot(state='True', action='VOOOOOM', type='Indian Red')"



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
