"""
Notes: =========================================================================
Notes: dictionary = {'key1':'value1', "key2":"value2"}  << Curly braces
Notes:
Notes: Access elements using square braces.
Notes:   Ex: dictionary['key3'] = 'value3'
Notes:
Notes: del dictionary['key4']
Notes:
Notes: dictionary.keys() returns all keys present in the directionary.
Notes:
Notes: dict() builds dictionaries directly from sequences of key-value pairs.
Notes:   Ex: dict([('Raghu', 18), ('Pavan', 21), ('Mohan', 36)])
Notes:   Ex: dict(Raghu=18, Pavan=21, Mohan=36)
Notes:
Notes: dict.iteritems()
Notes:    When looping through dictionaries, the key and corresponding value can
Notes:    be retrieved at the same time using the iteritems() method.
Notes:    Ex:   for k,v in dict.iteritems():
Notes:
Notes: in:
Notes:    To check whether a single key is in the dictionary, use "in" keyword.
Notes:
Notes: There is no guarantee about order of elements inside dictionary.
Notes:
"""

# create my dictionary
my_dict = { "Name": "Pavan Kumar Avala", "Age": "30", "Phone":"IPhone" }


# Add new element to dictionary
print "Dictionary before appending city: ", my_dict
my_dict["City"] = "New York"
print "Dictionary after  appending city: ", my_dict
print ""


# Print all keys.
print "Keys in dictionary: ", my_dict.keys()
print ""


# Del element from dictionary
print "Dictionary before deleting age : ", my_dict
del my_dict["Age"]
print "Dictionary after  deleting age : ", my_dict
print ""


# Build dictionary from sequence of key-value pairs.
new_dict = dict([('Raghu', 18), ('Pavan', 21), ('Mohan', 36)])
print "Dictionary from key-value pair :", new_dict
print ""


# When the keys are simple strings, specify pairs using keyword arguments.
new_dict = dict(Raghu=18, Pavan=21, Mohan=36)
print "Dictionary from key-value pair :", new_dict
print ""


# Find whether key is present in dictionaary.
print "Key \"Raghu\" Present in the dictionary? ", "Raghu" in new_dict
