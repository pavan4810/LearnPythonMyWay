"""
Notes: =========================================================================
Notes: A set is an unordered collection with no duplicate elements.
Notes:   Ex: set = {1, 4, 6, "Pavan"}
Notes:
Notes: Curly braces or the set() function can be used to create sets.
Notes:
Notes: To create an empty set, you have to use set(), not {}.
Notes:
Notes: Mathematical operations can be applied on sets.
Notes:   set1 + set2
Notes:   set1 - set2
Notes:   set1 & set2
Notes:   set1 | set2
Notes:   set1 ^ set2
Notes:
"""

emptySet = set()
print "emptySet:", emptySet
print ""

list1 = [0,1,2,3,4,5,6,7,8,9]
set1 = set(list1)
set2 = set((0,1,2,3,4,5))  # paranthesis
set3 = set([4,5,6,7,8,9])  # square braces
set4 = set({4,5})  # curly  braces
print "set1 :", set1
print "set2 :", set2
print "set3 :", set3
print "set4 :", set4
print ""



#===============================================================================
print "set2 & set3 :", set2 & set3
print "set2 - set3 :", set2 - set3
print "set2 | set3 :", set2 | set3
print "set2 - set4 :", set2 - set4
print "set3 - set4 :", set3 - set4
print "set3 ^ set4 :", set3 ^ set4

