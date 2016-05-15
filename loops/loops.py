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
Notes: enumerate()
Notes:    When looping through a sequence, the position index and corresponding
Notes:    value can be retrieved at the same time using the enumerate() function
Notes:    Ex:   for index, value in enumerate(range(1,10,2)):
Notes:              print index, value;
Notes:
Notes: zip()
Notes:    To loop over two or more sequences at the same time,
Notes:    the entries can be paired with the zip() function.
Notes:    Ex:   for a,b in zip(list1, list2):
Notes:
Notes: reverse()
Notes:    To loop over a sequence in reverse.
Notes:    Ex:   for a in reverse(list1):
Notes:
Notes: sorted()
Notes:    To loop over a sequence in sorted order.
Notes:    Ex:   for a in sorted(list1):
Notes:
Notes: iteritems()
Notes:    When looping through dictionaries, the key and corresponding value can
Notes:    be retrieved at the same time using the iteritems() method.
Notes:    Ex:   for k,v in dict.iteritems():
Notes:
"""

print "Looping over list                    :"
list = [1,2,5,8,9,3,20]
for number in list:
    print number,
print ""


#===============================================================================
print "Looping over range(x)                :"
for number in range(5):
    print number,
print ""


#===============================================================================
print "Looping over range(x,y)              :"
for number in range(1,5):
    print number,
print ""


#===============================================================================
print "Looping over range(x,y,increment)    :"
for number in range(1,10,2):
    print number,
print ""


#===============================================================================
print "Nested loop                          :"
for i in [[1,2,3], [4,5], [6,7,8,9]]:
   for j in i:
       print j,
   print ""
print ""


#===============================================================================
print "While loop                           :"
i = 0
while i < 5:
    print i,
    i += 1
print ""


#===============================================================================
print "Looping over range(x,y,increment) with enumerate   :"
for index, number in enumerate(range(1,10,2)):
    print index, number
print ""


#===============================================================================
list1 = [0,1,2,3,4,5]
list2 = [0,1,4,9,16,25]
print "Looping over with two sequences at the same time   :"
for a,b in zip(list1, list2):
    print a,b


#===============================================================================
print "Looping over dictionary elements                   :"
my_dict = {"Raghu":"Kota", "Pavan":"Avala", "Suresh":"Modi", "Sanfi":"Faria"}
for k,v in my_dict.iteritems():
    print k,v


