"""
Notes: =========================================================================
Notes: regular expression matching
Notes:      re.match() tries to match pattern at the begining of the string.
Notes:
Notes:      re.search() tries to search for pattern in entire string.
Notes: 
"""

import re
import optparse

def Main():
    parser = optparse.OptionParser("Usage %prog -w <word> -f <file>")

    # Add arguments
    parser.add_option("-w", dest="word", type='string',
                      help="Specify a word to search for")

    parser.add_option("-f", dest='fname', type='string',
                      help="Specify a file to search")


    # Parge arguments.
    (options, args) = parser.parse_args()

    if options.word == None or options.fname == None:
        print parser.usage
        exit(1)
    else:
        word = options.word
        filename = options.fname

    searchfile = open(filename)
    linenumber = 0

    for line in searchfile.readlines():
        line = line.strip("\n\r")
        linenumber += 1

        searchResult = re.search(word, line, re.M | re.I)
        if searchResult:
            print "%s : %s"%(str(linenumber), line)

    searchfile.close()


#===============================================================================
if __name__ == "__main__":
    Main()
