from functions import *

#===============================================================================
doNothing()
printSomething()
print sum(5,10);
print returnMultipleVariables(10, -20, 30)

try:
    __printModuleName()
except NameError:
    print 'As expected, names begining with "_" are not imported when',
    print '"from <module> import *" is used'

#===============================================================================
i = 5
def f(arg=i):
    print arg

i = 6
# f() return 5, not 6
f()


#===============================================================================
def f1(a, L=[]):
    L.append(a)
    return L

print f1(1)
print f1(2)
print f1(3)

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print f2(1)
print f2(2)
print f2(3)
