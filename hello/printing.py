print "Print using double quotes"
print 'Print using single quotes'
print "Observe how 'single quote' is used"
print 'Observe how "double quote" is used'

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
