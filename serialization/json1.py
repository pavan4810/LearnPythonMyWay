"""
Notes: =========================================================================
Notes: Serializing and de-serializing with Json
Notes:      json.dump(data, fileObject)
Notes:
Notes:      data = json.load(fileObject)
Notes:
Notes: Json does not support dictionaries.
Notes:
Notes: TODO: Json supports encoding of only one variable?
Notes:
"""

import json

dict1 = {"Name":"Pavan", "City":"Nashua", "Zip":3060}
#list1 = [10, 20, 30, 40, -1, -100 ]

print "Dict1 :", str(dict1)
#print "list1 :", str(list1)


# Serializing
with open("/tmp/json.d", "wb") as f:
    json.dump(dict1,f)
    #json.dump(list1,f)


# De-serializing
with open("/tmp/json.d", "rb") as f:
    dict2 = json.load(f)
    #list2 = json.load(f)


print "Dict2 :", str(dict2)
#print "list2 :", str(list2)
