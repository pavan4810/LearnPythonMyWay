"""
Notes: =========================================================================
Notes:  The subprocess module allows you to
Notes:      * spawn new processes,
Notes:      * connect to their input/output/error pipes, and
Notes:      * obtain their return codes
Notes:
Notes:  subprocess.call(args, *, stdin=None, stdout=None,
Notes:                           stderr=None, shell=False)
Notes:
Notes:      Run the command described by args,
Notes:      Wait for command to complete, then
Notes:      return the returncode attribute.
Notes:
Notes:      If first argument is "string command" and have spaces,
Notes:          then shell=True is required.
Notes:
Notes:      If first argument is a list, then shell=True is not required.
Notes:
Notes:      Using shell=True cab be security hazard.
Notes:
Notes:      Do not use stdout=PIPE or stderr=PIPE with this function as that
Notes:      can deadlock based on the child process output volume.
Notes:      Use Popen with the communicate() method when you need pipes.
Notes:
Notes:      So, finally best way to use subprocess.call is as follows
Notes:          subprocess.call([arg1, arg2, ...])
Notes:
Notes:
Notes:  Exceptions:
Notes:      CalledProcessError:
Notes:          if the called process returns a non-zero return code.
Notes:      ValueError:
Notes:          if Popen is called with invalid arguments.
Notes:      OSError:
Notes:          if trying to execute a non-existent file.
Notes:
"""

import subprocess


# Command with space, need shell=True
print "Output from : ", "subprocess.call('ls -l', shell=True)"
print "Return code ", subprocess.call("ls -l", shell=True)



# Note: There is a difference in o/p with and without shell=True
# Somehow, additional arguments are not being considered.
print "Output from : ", "subprocess.call(['ls', '-l'])"
print "Return code ", subprocess.call(['ls', '-l'])

print "Output from : ", "subprocess.call(['ls', '-l'], shell=False)"
print "Return code ", subprocess.call(['ls', '-l'], shell=False)

print "Output from : ", "subprocess.call(['ls', '-l'], shell=True)"
print "Return code ", subprocess.call(['ls', '-l'], shell=True)



# Command without space, no need of shell=True
# No difference in o/p.
print "Return code ", subprocess.call('ls')
print "Return code ", subprocess.call('ls', shell=False)
print "Return code ", subprocess.call('ls', shell=True)
print "Return code ", subprocess.call(['ls'])
print "Return code ", subprocess.call(['ls'], shell=False)
print "Return code ", subprocess.call(['ls'], shell=True)



# Following will fail
#print "Return code ", subprocess.call("ls -l")
#print "Return code ", subprocess.call("ls -l", shell=False)



# Unexpected exit with exit code other than 0
# Return code represents exit code.
print "Return code ", subprocess.call("exit 9", shell=True)
