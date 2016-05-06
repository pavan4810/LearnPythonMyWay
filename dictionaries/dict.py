"""
Notes: =========================================================================
Notes: dictionary = {'key1':'value1', "key2":"value2"}  << Curly braces
Notes:
Notes: dictionary['key3'] = 'value3' << access using square braces
Notes:
Notes: del dictionary['key4']
Notes:
Notes: There is not guarantee about order of elements inside dictionary.
"""

# create my dictionary
my_dict = { "Name": "Pavan Kumar Avala", "Age": "30", "Phone":"IPhone" }

# Add new element to dictionary
print "Dictionary before appending : ", my_dict
my_dict["City"] = "New York"
print "Dictionary after  appending : ", my_dict

# Del element from dictionary
print "Dictionary before deleting : ", my_dict
del my_dict["Age"]
print "Dictionary after  deleting : ", my_dict
