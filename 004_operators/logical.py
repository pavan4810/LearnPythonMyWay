"""
Notes: =========================================================================
Notes: expression1 and expression2:
Notes: expression1 or expression2:
Notes: not expression1
Notes: True
Notes: False
Notes:
"""

condition1 = True
condition2 = False

if condition1 and condition2:
    print "Both condition1 and condition2 are True"
elif condition1 or condition2:
    print "Either condition1 is True or condition2 is True, but not both"
else:
    print "Both condition1 and condition2 are False"

if not condition2:
    print "condition2 is False"
