"""
Notes: =========================================================================
Notes: value1 +  value2     (addition)
Notes: value1 -  value2     (substraction)
Notes: value1 *  value2     (multiplication)
Notes: value1 /  value2     (integer division)
Notes: value1 ** value2     (exponent)
Notes: value1 %  value2     (modulo)
Notes: Pay attention to % in format string
Notes:    print  "%d  %%  %d  =  %r" %(value1, value2, value1%value2)
Notes:
"""

value1 = 10
value2 = 3

print  "%r  +   %r   =  %r" %(value1, value2, value1+value2)
print  "%r  -   %r   =  %r" %(value1, value2, value1-value2)
print  "%r  *   %r   =  %r" %(value1, value2, value1*value2)
print  "%r  /   %r   =  %r" %(value1, value2, value1/value2)
print  "%r  / %r   =  %r" %(value1, float(value2), value1/float(value2))
print  "%r  **  %r   =  %r" %(value1, value2, value1**value2)
print  "%r  %%   %r   =  %r" %(value1, value2, value1%value2)
