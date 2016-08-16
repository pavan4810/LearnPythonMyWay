"""
Notes: =========================================================================
Notes: def function_name (arguments list):
Notes:      statement1
Notes:      ...
Notes:      statementN
Notes:      return x  # x can be single or multiple variables.
Notes:
"""

def doNothing():
    pass

def printSomething():
    print "Something"

def sum(operand1, operand2):
    tmp = operand1 + operand2
    return tmp


def returnMultipleVariables(arg1, arg2, arg3):
    return arg1, arg2, arg3


def __printModuleName():
    print "Module name: ",__name__


# write Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b


# return Fibonacci series up to n
def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


if __name__ == "__main__":
    doNothing()
    printSomething()
    print sum(5,10);
    print returnMultipleVariables(10, -20, 30)
    __printModuleName()
