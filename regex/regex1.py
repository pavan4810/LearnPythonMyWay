"""
Notes: =========================================================================
Notes: regular expression matching
Notes:      re.match() tries to match pattern at the begining of the string.
Notes: 
Notes:      re.search() tries to search for pattern in entire string.
Notes: 
Notes:      re.sub() tries to replace matched pattern and return new string.
Notes: 
Notes:      result.group() gives the matched string.
Notes: 
Notes:      <.*>   Greedy repetition: matches "<python>perl>".
Notes:      <.*?>  Nongreedy: matches "<python>" in "<python>perl>".
Notes: 
Notes: 
"""

import re

def Main():
    line = "I think, I think, I understand regular expression"

    #===========================================================================
    # re.match
    matchResult = re.match(r'think', line, re.M | re.I)

    if matchResult:
        print "Match found: ", matchResult.group()
    else:
        print "No match found"



    #===========================================================================
    # re.search
    searchResult = re.search(r'think', line, re.M | re.I)

    if searchResult:
        print "Search found: ", searchResult.group()
    else:
        print "No search found"




    #===========================================================================
    #    <.*>   Greedy repetition: matches "<python>perl>".
    #    <.*?>  Nongreedy: matches "<python>" in "<python>perl>".

    print "\n"
    line = "Cats are smarter than dogs"

    matchObj = re.match( r'(.*) are (.*?) (.*?) (.*)', line, re.M|re.I)
    if matchObj:
        print "matchObj.group()  : ", matchObj.group()
        print "matchObj.group(1) : ", matchObj.group(1)
        print "matchObj.group(2) : ", matchObj.group(2)
        print "matchObj.group(3) : ", matchObj.group(3)
        print "matchObj.group(4) : ", matchObj.group(4)
    else:
        print "No match!!"



    #===========================================================================
    #    ad+      No group    : + repeats \d.
    #    (ad)+    Grouped     : + repeats \D\d pair.

    print "\n"
    line = "adad"
    matchObj = re.search( r'ad+', line, re.M|re.I)
    if matchObj:
        print "matchObj.group()  : ", matchObj.group()
    else:
        print "No match!!"

    matchObj = re.search( r'(ad)+', line, re.M|re.I)
    if matchObj:
        print "matchObj.group()  : ", matchObj.group()
    else:
        print "No match!!"



    #===========================================================================
    phone = "2004-959-559 # This is Phone Number"

    print "\n"
    # Delete Python-style comments
    num = re.sub(r'#.*$', "", phone)
    print "Phone Num         : ", num

    # Remove anything other than digits
    num = re.sub(r'\D', "", phone)
    print "Phone Num         : ", num



#===============================================================================
if __name__ == "__main__":
    Main()
