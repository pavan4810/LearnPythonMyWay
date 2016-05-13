"""
Notes: =========================================================================
Notes: A tuple consists of a number of values separated by commas.
Notes:   Ex: tuple = (1, 4, 6, "Pavan")
Notes:
Notes: Tuples can be nested.
Notes:   Ex: tuple1 = (tuple2, tuple3)
Notes:
Notes: Tuples are immutable.
Notes:   Ex: tuple[0] = "something" is not valid
Notes:
Notes: Tuple with 0 or 1 element are specials.
Notes:   Empty tuple is constructed by empty pair of paranthesis.
Notes:   Tuple with one item is constructed by following a value with a comma.
Notes:
"""

myTuple = (1,2,3,"Pavan")
print "Tuple:", myTuple
print ""


#===============================================================================
# Nested tuples.
tuple1 = (1,2,3)
tuple2 = (4,5,6)
myTuple = (tuple1, tuple2)
print "Tuple from two lists:", myTuple
for x in myTuple:
    print x,
print "\n"


#===============================================================================
# Empty tuple and single element tuple.
emptytuple = ()
singleton = ('pavan',)

print "Empty tuple", emptytuple
print "Single element tuple", singleton
print ""


#===============================================================================
# Packing.
myTuple = (1,2,3,"Pavan")
print myTuple


#===============================================================================
# Unpacking.
x,y,z,name = myTuple
print x,y,z,name
