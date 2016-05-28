"""
Notes: =========================================================================
Notes: shutil module
Notes:
Notes:      shutil.copy()
Notes:      shutil.copy2()
Notes:      shutil.copyfile()
Notes:      shutil.errno()
Notes:      shutil.move()
Notes:      shutil.stat()
Notes:
"""

import shutil

# Get to know about module shutil content
print dir(shutil)

shutil.copyfile('./lib_shutil.py', './tmp2.py')
shutil.move('./tmp2.py', './tmp4.py')
