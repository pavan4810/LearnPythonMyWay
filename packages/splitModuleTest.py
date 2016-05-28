"""
Notes: =========================================================================
Notes: Splitting a module.
Notes:      Lets split module.py into two files, one for each class definition.
Notes:
Notes:      To do that, start by replacing the module.py file with a directory
Notes:      called mymodule.
Notes:
Notes:      In that directory, create the following files.
Notes:          module/
Notes:              __init__.py
Notes:              a.py
Notes:              b.py
Notes:
Notes:      # a.py
Notes:          class A:
Notes:              def spam(self):
Notes:                  print('A.spam')
Notes:
Notes:      # b.py
Notes:          from .a import A
Notes:          class B(A):
Notes:              def bar(self):
Notes:                  print('B.bar')
Notes:
Notes:      Finally, in the __init__.py file, glue the two files together:
Notes:          # __init__.py
Notes:              from .a import A
Notes:              from .b import B
Notes:
Notes:
"""

import splitModule as dut

a = dut.A()
a.spam()

b = dut.B()
b.bar()
