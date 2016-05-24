"""
Notes: =========================================================================
Notes: regular expression matching
Notes:      re.match() tries to match pattern at the begining of the string.
Notes:
Notes:      re.search() tries to search for pattern in entire string.
Notes: 
"""

import re

def Main():
    line = "I think I understand regular expression"

    # re.match
    matchResult = re.match(r'think', line, re.M | re.I)

    if matchResult:
        print "Match found: ", matchResult.group()
    else:
        print "No match found"


    # re.search
    searchResult = re.search(r'think', line, re.M | re.I)

    if searchResult:
        print "Search found: ", searchResult.group()
    else:
        print "No search found"



#===============================================================================
if __name__ == "__main__":
    Main()
