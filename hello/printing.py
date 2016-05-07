print "Print using double quotes"
print 'Print using single quotes'
print "Observe how 'single quote' is used"
print 'Observe how "double quote" is used'

print """
  Three double-quotes are used
  to print multi-line text.
  We'll be able to print as much as we like.
"""

cars = 100
bikes = 2000
city = "Akividu"

# Without using format string 
print "There are", cars, "cars", "and", bikes, "bikes available"

# Using format string and variables
print "There are %d cars and %d bikes available in city %s" %(cars, bikes, city)

# Using format string and variables
print "There are %d cars" %(cars), "and %d bikes available in city %s" %(bikes, city)

# To print variable value no matter what variable type, use %r
# Observe single quotes around variable value printed with %r
print "There are %r cars and %r bikes available in city %r" %(cars, bikes, city)

string="Single quotes"
print "Observe %r around variable value printed with %%r" %(string)

char01 = "P"
char02 = "a"
char03 = "v"
char04 = "a"
char05 = "n"
char06 = "K"
char07 = "u"
char08 = "m"
char09 = "a"
char10 = "r"

# watch that comma at the end. It helps in continuation of printing
print char01 + char02 + char03 + char04 + char05,
print char06 + char07 + char08 + char09 + char10
