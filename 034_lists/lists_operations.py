"""
Notes: =========================================================================
Notes: len(list)
Notes:   This function gives size of list.
Notes:
Notes: list.insert(position, value)
Notes:   Insert an item at a given position.
Notes:
Notes: list.append(list element)
Notes:   This function appends elements to list.
Notes:   a.append(x)  equivalent to  a[len(a):] = [x]
Notes:   a.append(x)  equivalent to  a.insert(len(a), x)
Notes:
Notes: list.extend(list2)
Notes:   Extend the list by appending all the items in the given list;
Notes:   equivalent to       a[len(a):] = L
Notes:
Notes: list.remove(x)
Notes:   Remove the first item from the list whose value is x.
Notes:   It is an error if there is no such item.
Notes: 
Notes: list.pop(index)
Notes:   This function pops an element from the list.
Notes:   If no index is specified, a.pop() removes and returns the last item.
Notes:   Ex: list.pop(0), list.pop(), list.pop(1), list.pop(-1) list.pop(-2)
Notes:
Notes: list.index(x)
Notes:   Return the index in the list of the first item whose value is x.
Notes:   It is an error if there is no such item.
Notes:
Notes: list.count(x)
Notes:   Return the number of times x appears in the list.
Notes:
Notes: list.reverse()
Notes:   Reverse the elements of the list, in place.
Notes:
Notes: list.sort(cmp=None, key=None, reverse=False)
Notes:   Sort the items of the list in place (the arguments can be used for
Notes:   sort customization, see sorted() for their explanation).
Notes:
"""

#===============================================================================
name = ["Pavan", "Kumar", "Avala"]
print "List : ", name
print "List length : ", len(name)
print ""


#===============================================================================
name = []
print "List before inserting : ", name
name.insert(0, "Pavan")
name.insert(1, "Kumar")
name.insert(2, "Avala")
print "List after  inserting : ", name
print ""


#===============================================================================
name = ["Pavan", "Kumar", "Avala"]
print "List before appending : ", name
name.append("The")
name[len(name):] = ["Great"]
print "List after  appending : ", name
print ""


#===============================================================================
name = ["Pavan", "Kumar", "Avala"]
print "List before extending : ", name
extention = ["The", "Great"]
name.extend(extention)
print "List after  extending : ", name
print ""


#===============================================================================
name = ["Pavan", "Kumar", "Avala", "The", "Great"]
print "List before removing  : ", name
name.remove("The")
name.remove("Great")
print "List after  removing  : ", name
print ""



#===============================================================================
name = ["Pavan", "Kumar", "Avala", "The", "Great"]
print "List before poping    : ", name
name.pop(3)         # Pops "The"
name.pop()          # Pops last element "Great"
name.pop(-2)        # Pops second last element "Kumar"
print "List after  poping    : ", name
print ""



#===============================================================================
name = ["Pavan", "Kumar", "Avala", "The", "Great"]
print "List =", name
print "\"Avala\" is at index ", name.index("Avala")
print ""



#===============================================================================
name = ["Pavan", "Pavan", "Kumar", "Kumar", "Kumar"]
print "List =", name
print "\"Kumar\" is present %d times" %name.count("Kumar")
print ""



#===============================================================================
name = ["Pavan", "Kumar", "Avala"]
print "List          =", name
name.reverse()
print "Reversed list =", name
print ""



#===============================================================================
name = ["Pavan", "Kumar", "Avala"]
print "List          =", name
name.sort()
print "Sorted   list =", name
print ""

