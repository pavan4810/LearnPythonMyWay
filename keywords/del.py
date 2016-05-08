"""
Notes: =========================================================================
Notes: del <thing to be deleted>
Notes:      del list[4]
Notes:      del list
Notes:      del dict['key']
Notes:      del dict
Notes:      del variable
Notes:      del function
"""

print "Before adding function1\n", dir()
def function1():
  pass
print "After adding function1\n", dir()
del function1
print "After deleting function1\n", dir()

print ""
mylist = [0,1,1,2,3,5,8,13,21]
print "Before deleting elemets", mylist
del mylist[3]
print "After deleting 4th element", mylist
del mylist

print ""
dictionary = {"Name":"Pavan", "Age":30, "City":"Akividu"}
print "Before deleting any element", dictionary
del dictionary["Age"]
print "After deleting Age element from dictionary", dictionary
del dictionary

print ""
print "Before adding variable foo\n", dir()
foo = 5
print "After adding variable foo\n", dir()
del foo
print "After deleting variable foo\n", dir()
