"""
Notes: =========================================================================
Notes: Serializing and de-serializing with pickle
Notes:      pickle.dump(data, fileObject)
Notes:
Notes:      data = pickle.load(fileObject)
Notes:
"""

import pickle

dict1 = {"Name":"Pavan", "City":"Nashua", "Zip":3060}
list1 = [10, 20, 30, 40, -1, -100]

print "Dict1 :", str(dict1)
print "list1 :", str(list1)


# Serializing
with open("/tmp/pickle.d", "wb") as f:
    pickle.dump(dict1,f)
    pickle.dump(list1,f)


# De-serializing
with open("/tmp/pickle.d", "rb") as f:
    dict2 = pickle.load(f)
    list2 = pickle.load(f)


print "Dict2 :", str(dict2)
print "list2 :", str(list2)
