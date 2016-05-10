"""
Notes: =========================================================================
Notes: list[0]   :  Returns item in 0th position
Notes: list[5]   :  Returns item in 5th position
Notes:
Notes:           :  Slicing always returns new list
Notes: list[-3:] :  New list with last three elements
Notes:
Notes: list[:]   :  New list with all elements. It is like duplicating a list.
Notes:
Notes: list[:2]  :  Elements from begining     (included) to   2 (excluded)
Notes: list[2:]  :  Elements from position 2   (included) to end (included)
Notes: list[-2:] :  Elements from second last  (included) to end (included)
Notes:
Notes:           :  Lists also supports operations like concatenation.
Notes: list1 + list2
Notes:
Notes:           :  Lists also mutable (but, string are immutable)
Notes: list1[x]  =  y
Notes:
Notes:           :  Assignment to slices is also possible, and this can even
Notes:           :  change the size of the list or clear it entirely.
Notes:
Notes: list[2:5] = [1, 5, 10]
Notes: list[2:5] = []
Notes: list[:]   = []
Notes:
Notes:           : It is possible to nest lists.
Notes: list      = [list1, list2]
Notes: list[x][y]
Notes:
"""
print " list[0]   :  Returns item in 0th position"
print " list[5]   :  Returns item in 5th position"
print ""
print "           :  Slicing always returns new list"
print " list[-3:] :  New list with last three elements"
print ""
print " list[:]   :  New list with all elements. It is like duplicating a list."
print ""
print " list[:2]  :  Elements from begining     (included) to   2 (excluded)"
print " list[2:]  :  Elements from position 2   (included) to end (included)"
print " list[-2:] :  Elements from second last  (included) to end (included)"
print ""
print "           :  Lists also supports operations like concatenation."
print " list1 + list2"
print ""
print "           :  Lists also mutable (but, string are immutable)"
print " list1[x]  =  y"
print ""
print "           :  Assignment to slices is also possible, and this can even"
print "           :  change the size of the list or clear it entirely."
print ""
print " list[2:5] = [1, 5, 10]"
print " list[2:5] = []"
print " list[:]   = []"
print ""
print "           : It is possible to nest lists."
print " list      = [list1, list2]"
print " list[x][y]"
