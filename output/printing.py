"""
Notes: =========================================================================
Notes:  print can be used with single quotes or double quotes.
Notes:
Notes:  str.format()
Notes:      print 'Pavan {} Avala the {}!'.format('Kumar', 'Great')
Notes:
Notes:  str.rjust(x)
Notes:  str.ljust(x)
Notes:  str.center(x)
Notes:
Notes:  str.zfill()
Notes:      Pads a numeric string on the left with zeros.
Notes:      It understands about plus and minus signs.
Notes:
"""

print "Print using double quotes"
print 'Print using single quotes'
print "Observe how 'single quote' is used"
print 'Observe how "double quote" is used'
print ""
print """
  Three double-quotes are used
  to print multi-line text.
  We'll be able to print as much as we like.
"""

#===============================================================================
cars = 100
bikes = 2000
city = "Akividu"

# Without using format string 
print "There are", cars, "cars", "and", bikes, "bikes available"

# Using format string and variables
print "There are %d cars and %d bikes available in city %s" %(cars, bikes, city)

# Using format string and variables
print "There are %d cars" %(cars), "and %d bikes available in city %s" %(bikes, city)


#===============================================================================
# To print variable value no matter what variable type, use %r
# Observe single quotes around variable value printed with %r
print "There are %r cars and %r bikes available in city %r" %(cars, bikes, city)

string="Single quotes"
print "Observe %r around variable value printed with %%r" %(string)


#===============================================================================
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



#===============================================================================
# Fancy output formatting
print "The story of {0} {1} programming language {other}.".format('Pavan', 'Learning', other='Python')

# Fancy output formatting with spaces
print "The story of {0:10s} {1:10s} programming language {other:20s}.".format('Pavan', 'Learning', other='Python')

# Fancy output formatting with spaces
print "The story of {0:10s} {1:10s} {3:20s} in {2:2s} days.".format('Pavan', 'Learning', '7', 'Python')



#===============================================================================
# Fancy output formatting with spaces - rjust(#ofspaces), ljust(#ofspaces)
print "The story of %s %s %s in %s days." %(repr("Pavan").ljust(10),
                                            repr("Learning").ljust(20),
                                            repr("Python").ljust(10),
                                            repr(7).ljust(2))

# Fancy output formatting with spaces - rjust(#ofspaces), ljust(#ofspaces)
print "The story of %s %s %s in %s days." %(repr("Pavan").center(10),
                                            repr("Learning").center(20),
                                            repr("Python").center(10),
                                            repr(7).center(2))

# Fancy output formatting with spaces - rjust(#ofspaces), ljust(#ofspaces)
print "The story of %s %s %s in %s days." %(repr("Pavan").rjust(10),
                                            repr("Learning").rjust(20),
                                            repr("Python").rjust(10),
                                            repr(7).rjust(2))

#left adjust
for x in range(1, 10):
    print repr(x).ljust(2), repr(x*x).ljust(3),
    # Note trailing comma on previous line, which help in continuation of printing
    print repr(x*x*x).ljust(4)

#right adjust
for x in range(1, 10):
    print repr(x).rjust(2), repr(x*x).rjust(3),
    # Note trailing comma on previous line, which help in continuation of printing
    print repr(x*x*x).rjust(4)
print ""


#===============================================================================
numeric_string = '12'
print numeric_string.zfill(5)

numeric_string = '-3.14'
print numeric_string.zfill(7)

numeric_string = '3.14159265359'
print numeric_string.zfill(5)
