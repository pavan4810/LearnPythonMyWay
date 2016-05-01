"""
Notes: =========================================================================
Notes: list = [1,2,5,8,9,3,20]
Notes: for number in list:
Notes:
Notes: for number in range(30):
Notes: for number in range(1,20):
Notes: for number in range(1,20,2):
Notes:
Notes; for i in [[1,2,3], [4,5], [6,7,8,9]]:
Notes:    for j in i:
Notes:
Notes: while condition:
Notes:    statements
Notes:
"""

print "Looping over list                    :"
list = [1,2,5,8,9,3,20]
for number in list:
    print number

print "Looping over range(x)                :"
for number in range(5):
    print number

print "Looping over range(x,y)              :"
for number in range(1,5):
    print number

print "Looping over range(x,y,increment)    :"
for number in range(1,10,2):
    print number

print "Nested loop                          :"
for i in [[1,2,3], [4,5], [6,7,8,9]]:
   for j in i:
       print j

print "While loop                           :"
i = 0
while i < 5:
    print i
    i += 1
