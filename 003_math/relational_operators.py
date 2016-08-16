"""
Notes: =========================================================================
Notes: value1 == value2:
Notes: value1 != value2:
Notes: value1 > value2:
Notes: value1 < value2:
Notes: value1 >= value2:
Notes: value1 <= value2:
Notes:
"""

value1 = 10
value2 = 20
value3 = 30

if value1 == value2 and value1 != value3:
    print "Both value1 and value2 are equal, but not equal to value3"
elif value1 > value2:
    if value1 >= value3:
        print "Value1 is greater than value2. And, greater than or equal to value3"
    else:
        print "Value1 is greater than value2. But, less than value3"
elif value1 < value2:
    if value2 >= value3:
        print "Value2 is greater than value1. And, greater than or equal to value3"
    else:
        print "Value2 is greater than value1. But, less than value3"
    print "Value1 is less than value2"
else:
    print "All values are equal"
