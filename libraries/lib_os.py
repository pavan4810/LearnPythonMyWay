"""
Notes: =========================================================================
Notes: OS Module
Notes:      os.abort()
Notes:
Notes:      os.chmod()
Notes:      os.chown()
Notes:      os.chroot()
Notes:      os.chdir()
Notes:      os.curdir()
Notes:
Notes:      os.dup()
Notes:      os.dup2()
Notes:
Notes:      os.execl()
Notes:      os.execle()
Notes:      os.execlp()
Notes:      os.execlpe()
Notes:      os.execv()
Notes:      os.execve()
Notes:      os.execvp()
Notes:      os.execvpe()
Notes:      os.fork()
Notes:
Notes:      os.fdopen()
Notes:      os.fstat()
Notes:      os.fsync()
Notes:      os.ftruncate()
Notes:
Notes:      os.getcwd()
Notes:      os.getenv()
Notes:      os.getpgid()
Notes:      os.getpgrp()
Notes:      os.getpid()
Notes:      os.getppid()
Notes:
Notes:      os.lseek()
Notes:
Notes:      os.mkdir()
Notes:      os.mkfifo()
Notes:
Notes:      os.open()
Notes:      os.pipe()
Notes:      os.popen()
Notes:
Notes:      os.read()
Notes:      os.rename()
Notes:      os.rmdir()
Notes:
Notes:      os.stat()
Notes:      os.system()
Notes:
Notes:      os.umask()
Notes:      os.uname()
Notes:      os.utime()
Notes:
Notes:      os.waitpid()
Notes:
"""

import os

# Get to know module content
print dir(os)
#help(os)

# Example usage
print os.getcwd()

os.chdir("../")

print os.urandom(2)
