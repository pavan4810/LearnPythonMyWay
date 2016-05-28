"""
Notes: =========================================================================
Notes: Packaging in Python:
Notes:
Notes:      In that directory, create the following files.
Notes:          packing/
Notes:              __init__.py
Notes:              module1/
Notes:                  __init__.py
Notes:                  file1.py
Notes:                  file2.py
Notes:              module2/
Notes:                  __init__.py
Notes:                  file3.py
Notes:                  file4.py
Notes:
Notes:      # file1.py
Notes:          def Func1():
Notes:              print "Inside Func1()"
Notes:
Notes:      # file2.py
Notes:          from ..module2 import *
Notes:          def Func2():
Notes:                print "Inside Func2()"
Notes:                    print "\tCalling Func4()"
Notes:                    file2.Func4()
Notes:
Notes:      Glue files in module1 folder using __init__.py
Notes:          # __init__.py
Notes:              from .file1 import *
Notes:              from .file2 import *
Notes:
Notes:
Notes:      # file3.py
Notes:          from ..module1 import *
Notes:              
Notes:          def Func3():
Notes:                print "Inside Func3()"
Notes:                    print "\tCalling Func1()"
Notes:                    file1.Func1()
Notes:
Notes:      # file4.py
Notes:          def Func4():
Notes:              print "Inside Func4()"
Notes:
Notes:      Glue files in module2 folder using __init__.py
Notes:          # __init__.py
Notes:              from .file1 import *
Notes:              from .file2 import *
Notes:
Notes:      Finally, in the __init__.py file, glue all subfolder:
Notes:          # __init__.py
Notes:              from .module1 import *
Notes:              from .module2 import *
Notes:
"""

import packing as dut

dut.Func1()
print "============================"

dut.Func2()
print "============================"

dut.Func3()
print "============================"

dut.Func4()
print "============================"
