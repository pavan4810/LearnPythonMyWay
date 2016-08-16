"""
Notes: =========================================================================
Notes: from sys import argv
Notes: print argv
Notes:
"""

from sys import argv

print argv

for i in argv:
    if i=="None":
        break
    print i

#For three argument programs
#script, first, second, third = argv
#print script, first, second, third
