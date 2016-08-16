"""
Notes: =========================================================================
Notes: str(variable)
Notes:  Meant to return representations of values which fairly human-readable.
Notes:
Notes: repr(variable)
Notes:  Meant to generate representations which can be read by the interpreter.
Notes:
Notes: For objects which don't have a particular representation for human
Notes: consumption, str() will return the same value as repr().
Notes:
Notes: Many values, such as numbers or structures like lists and dictionaries,
Notes: have the same representation using either function.
Notes:
Notes: Strings and floating point numbers, have two distinct representations.
Notes:
"""

my_int    = 10
my_list   = [10,5,"Pavan",3.3]
my_dict   = {"Name":"Pavan", "Age":31, "Home":"Akividu"}
my_tuple  = (2, 3.3, "Kumar")
my_string = "Pavan Kumar Avala"
my_float  = 1.0/7.0

print "my_int    : ", my_int
print "my_list   : ", my_list
print "my_dict   : ", my_dict
print "my_tuple  : ", my_tuple
print "my_string : ", my_string
print "my_float  : ", my_float

print "\nStr version"
print "my_int    : ", str(my_int)
print "my_list   : ", str(my_list)
print "my_dict   : ", str(my_dict)
print "my_tuple  : ", str(my_tuple)
print "my_string : ", str(my_string)
print "my_float  : ", str(my_float)

print "\nrepr version"
print "my_int    : ", repr(my_int)
print "my_list   : ", repr(my_list)
print "my_dict   : ", repr(my_dict)
print "my_tuple  : ", repr(my_tuple)
print "my_string : ", repr(my_string)
print "my_float  : ", repr(my_float)
