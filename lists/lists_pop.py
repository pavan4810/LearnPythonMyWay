"""
Notes: =========================================================================
Notes: list.pop(index)
Notes:   This function pops an element from the list.
Notes:   Ex: list.pop(0), list.pop(1), list.pop(-1) list.pop(-2)
Notes:
"""

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
