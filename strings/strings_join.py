"""
Notes: =========================================================================
Notes: separator_character.join(list of words)
Notes:   Ex:  ' '.join(input), ':'.join(input), '/'.join(input)
Notes:
"""

# Input list
input_list = ["Pavan", "Kumar", "Avala", "is", "Great"]

# join using ' ' as separator
stuff = ' '.join(input_list)
print stuff

# join using ':' as separator
stuff = ':'.join(input_list)
print stuff

# join using '/' as separator
stuff = '/'.join(input_list)
print stuff



# Input list
input_list = ['P', 'a', 'v', 'a', 'n']

# join using ' ' as separator
stuff = ' '.join(input_list)
print stuff

# Input list
input_list = ['P', 'a', 'v', 'a', 'n']

# join using '' as separator
stuff = ''.join(input_list)
print stuff


#===============================================================================
# string concatenation
print 3*"Pavan " + 2 * "Kumar " + 1 * "Avala"

# It becomes a single string, without comma.
name = ('Pavan '
        'Kumar '
        'Avala')
print name

name = ('Pavan ',
        'Kumar ',
        'Avala')
print name
