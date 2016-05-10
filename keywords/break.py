"""
Notes: =========================================================================
Notes: break    :
Notes:          The break statement, like in C, breaks out of the smallest
Notes:          enclosing for or while loop
Notes:          a loop's "else" clause runs when no break occurs.
Notes:
Notes: continue :
Notes:          The continue statement, also borrowed from C, continues with the
Notes:          next iteration of the loop.
Notes:
Notes: pass     :
Notes:          The pass statement does nothing. It can be used when a statement
Notes:          is required syntactically but the program requires no action.
Notes:
"""

#===============================================================================
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'


#===============================================================================
for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found an odd number", num



#===============================================================================
def MyEmptyClass():
    print "Inside function\n"
    pass

MyEmptyClass()
