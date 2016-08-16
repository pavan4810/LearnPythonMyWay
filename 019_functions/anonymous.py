"""
Notes: =========================================================================
Notes: lamda    : creates new shorthand function definition.
Notes:      function_pointer = lambda x:f(x)
Notes:      function_pointer(x)
Notes:
Notes: map      : Each element in the list is provided as argument to the
Notes:            function pointer and new list is formed with all return values
Notes:
Notes:      return_list = map(function_pointer, input_list)
Notes:      return_list = map(cube, range(1,10))
Notes:
Notes:
Notes: filter   : each element in the list is provided as argument to function
Notes:            pointer and returns subset of input list for which function
Notes:            pointer returns True
Notes:
Notes:      return_list = filter(function_pointer, input_list)
Notes:      return_list = filter((lambda x:x%2), [0,1,1,2,3,5,8,13,21,34,55])
Notes:
Notes:
Notes: reduce   : First two elements in the input list are provided as arguments
Notes:            to the function pointer and are replaced with return value.
Notes:            This procedure is followed recursively on all elements in the
Notes,            list till only one element is present in the list.
Notes:
Notes:      return_value = reduce(function_pointer, input_list)
Notes:      return_value = reduce((lambda x,y:x+y), [1,2,3,4,5,6,7,8,9])
"""

#===============================================================================
square = lambda x: x*x
cube   = lambda x: x*x*x
print square(5)
print cube(3)


#===============================================================================
def cubeFunction(x):
    return x*x*x

y = map(cubeFunction, range(1,10))
print y


#===============================================================================
y = filter((lambda x:x%2), [0,1,1,2,3,5,8,13,21,34,55,89])
print y


#===============================================================================
z = reduce((lambda x,y: x+y), [1,2,3,4,5,6,7,8,9])
print z
