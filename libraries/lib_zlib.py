"""
Notes: =========================================================================
Notes: zlib module:
Notes:
Notes:      zlib.compress
Notes:      zlib.crc32
Notes:      zlib.decompress
Notes:
"""

import zlib

# Get to know about module zlib content
print "========================================================================"
print "zlib Module : start"
print dir(zlib)
print "zlib Module : end"
print "========================================================================"

s = 'witch which has which witches wrist watch'
print "String          : ", s
print "Length of string: ", len(s)

t = zlib.compress(s)
print "Compressed      : ", t
print "Length of string: ", len(t)

print "Decompressed    : ", zlib.decompress(t)
print "CRC32           : ", zlib.crc32(s)
