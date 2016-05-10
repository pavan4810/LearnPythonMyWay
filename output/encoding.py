# To print UNICODE data, use "u" before format string
print "To print UNICODE data, use \"u\" before format string"

# \u0020 == Space
print u"Hello\u0020World !"



# By appending r before the first quote, characters prefaced by \ will not be
# interpreted as special characters.
print r"By appending r before the first quote, characters prefaced by \ will not be"
print "interpreted as special characters. Observe following two"
print r"What is your \name!"
print "What is your \name!"



print "'u' and 'r' can be used together before the first quote"
print ur'Hello\u0020World !'
