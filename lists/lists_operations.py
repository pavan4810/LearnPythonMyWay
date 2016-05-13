"""
Notes: =========================================================================
Notes: len(list)
Notes:   This function gives size of list.
Notes:
Notes: list.append(list element)
Notes:   This function appends elements to list.
Notes:   This is equal to    a[len(a):] = [x]
Notes:
Notes: list.extend(list2)
Notes:   Extend the list by appending all the items in the given list;
Notes:   equivalent to       a[len(a):] = L
Notes:
Notes: list.pop(index)
Notes:   This function pops an element from the list.
Notes:   Ex: list.pop(0), list.pop(1), list.pop(-1) list.pop(-2)
Notes:
"""

#===============================================================================
name = ["Pavan", "Kumar", "Avala"]
print "List : ", name
print "List length : ", len(name)
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
def pop_a_word(words, index):
    """ This function pops a word from specified index."""
    return words.pop(index)

words = ["Avala", "Pavan", "Kumar"]
print "List before poping a word from index %d:\n\t" %(0), words
pop_a_word(words, 0)
print "List after poping a word from index %d:\n\t" %(0), words, "\n"

words = ["Pavan", "Kumar", "Avala"]
print "List before poping a word from index %d:\n\t" %(-1), words
pop_a_word(words, -1)
print "List after poping a word from index %d:\n\t" %(-1), words, "\n"

words = ["Pavan", "Kumar", "Avala"]
print "List before poping a word from index %d:\n\t" %(1), words
pop_a_word(words, 1)
print "List after poping a word from index %d:\n\t" %(1), words, "\n"

words = ["Pavan", "Kumar", "Avala"]
print "List before poping a word from index %d:\n\t" %(-2), words
pop_a_word(words, -2)
print "List after poping a word from index %d:\n\t" %(-2), words, "\n"
