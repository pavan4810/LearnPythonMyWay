"""
Notes: =========================================================================
Notes: subprocess.check_call(args, *, stdin=None, stdout=None,
Notes:                           stderr=None, shell=False)
Notes:
Notes:      Run the command described by args,
Notes:      Wait for command to complete, then
Notes:
Notes:      If the return code was zero then return,
Notes:      otherwise raise CalledProcessError. The CalledProcessError object
Notes:      will have the return code in the returncode attribute.
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
Notes:      So, best way to use subprocess.call is as follows
Notes:          subprocess.check_call([arg1, arg2, ...])
otes:
Notes: TODO : Explore more about subprocess.check_call()
"""

import subprocess

# Command with space in it, need shell=True
print "\nsubprocess.check_call('ls -l', shell=True) has returned",\
      subprocess.check_call("ls -l", shell=True)

print "\nsubprocess.check_call(['ls', '-l']) has returned",\
      subprocess.check_call(['ls', '-l'])



#===============================================================================
# Ideally, I expect following three to raise same exception, but seems not.
try:
    returncode = subprocess.check_call(['exit', '9'])
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_call(['exit', '9']) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_call(['exit', '9']) has raised "+\
          "different exception"
else:
    print "\nsubprocess.check_call(['exit', '9']) has returned :",\
          returncode

try:
    returncode = subprocess.check_call(['exit', '9'], shell=True)
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_call(['exit', '9'], shell=True) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_call(['exit', '9'], shell=True) has raised "+\
          "different exception"
else:
    print "\nsubprocess.check_call(['exit', '9'], shell=True) has returned :",\
          returncode


try:
    returncode = subprocess.check_call('exit 9', shell=True)
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_call('exit 9', shell=True) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_call('exit 9', shell=True) has raised "+\
          "different exception"
else:
    print "\nsubprocess.check_call('exit 9', shell=True) has returned :",\
          returncode
print ""


#===============================================================================
# Ideally, I expect following three to raise same exception, but seems not.
try:
    returncode = subprocess.check_call(['exit', '0'])
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_call(['exit', '0']) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_call(['exit', '0']) has raised "+\
           "different exception"
else:
    print "\nsubprocess.check_call(['exit', '0']) has returned",\
          returncode


try:
    returncode = subprocess.check_call(['exit', '0'], shell=True)
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_call(['exit', '0'], shell=True) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_call(['exit', '0'], shell=True) has raised "+\
           "different exception"
else:
    print "\nsubprocess.check_call(['exit', '0'], shell=True) has returned",\
          returncode


try:
    returncode = subprocess.check_call('exit 0', shell=True)
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_call('exit 0', shell=True) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_call('exit 0', shell=True) has raised "+\
          "different exception"
else:
    print "\nsubprocess.check_call('exit 0', shell=True) has returned",\
          returncode
print ""


#===============================================================================
try:
    returncode = subprocess.check_call('ls pavan', shell=True)
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_call('ls pavan', shell=True) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_call('ls pavan', shell=True) has raised "+\
          "different exception"
else:
    print "\nsubprocess.check_call('ls pavan', shell=True) has returned :",\
          returncode

try:
    returncode = subprocess.check_call(['ls', 'pavan'])
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_call(['ls', 'pavan']) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_call(['ls', 'pavan']) has raised "+\
          "different exception"
else:
    print "\nsubprocess.check_call(['ls', 'pavan']) has returned :",\
          returncode
