"""
Notes: =========================================================================
Notes: if expression:
Notes:     action1
Notes:     ....
Notes:     actionX
Notes: elif expression:
Notes:     action1
Notes:     ....
Notes:     actionY
Notes: else:
Notes:     action1
Notes:     ....
Notes:     actionZ
Notes:
"""

condition1 = 0
condition2 = 1

if condition1:
    print "Condition1 is TRUE"
elif condition2:
    print "Condition1 is FALSE, but condition2 is TRUE"
else:
    print "Both condition1 and condition2 are FALSE"
