"""
Notes: =========================================================================
Notes: subprocess.check_output(args, *, stdin=None, stdout=None, stderr=None,
Notes:                                  shell=False, universal_newlines=False)
Notes:
Notes:      Run the command with args and return its ouput as a byte string.
Notes:      Wait for command to complete, then
Notes:
Notes:      If the return code was non-zero, it raises a CalledProcessError.
Notes:      The CalledProcessError object will have the return code in the
Notes:      "returncode" attribute and any output in "output" attribute.
Notes:
Notes:      If first argument is "string command" and have spaces in it,
Notes:      then shell=True is required.
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
Notes:          subprocess.check_output([arg1, arg2, ...])
otes:
Notes: TODO : Explore more about subprocess.check_output()
Notes:
"""

import subprocess

# Command with space in it, need shell=True
print "\nsubprocess.check_output('ls -l', shell=True) has returned :",\
      subprocess.check_output("ls -l", shell=True)

print "\nsubprocess.check_output(['ls', '-l']) has returned :",\
      subprocess.check_output(['ls', '-l'])



#===============================================================================
# Ideally, I expect following three to raise same exception, but seems not.
try:
    returncode = subprocess.check_output(['exit', '9'])
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_output(['exit', '9']) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_output(['exit', '9']) has raised "+\
          "different exception"
else:
    print "\nsubprocess.check_output(['exit', '9']) has returned :",\
          returncode

try:
    returncode = subprocess.check_output(['exit', '9'], shell=True)
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_output(['exit', '9'], shell=True) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_output(['exit', '9'], shell=True) has raised "+\
          "different exception"
else:
    print "\nsubprocess.check_output(['exit', '9'], shell=True) has returned :",\
          returncode


try:
    returncode = subprocess.check_output('exit 9', shell=True)
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_output('exit 9', shell=True) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_output('exit 9', shell=True) has raised "+\
          "different exception"
else:
    print "\nsubprocess.check_output('exit 9', shell=True) has returned :",\
          returncode
print ""


#===============================================================================
# Ideally, I expect following three to raise same exception, but seems not.
try:
    returncode = subprocess.check_output(['exit', '0'])
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_output(['exit', '0']) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_output(['exit', '0']) has raised "+\
           "different exception"
else:
    print "\nsubprocess.check_output(['exit', '0']) has returned :",\
          returncode


try:
    returncode = subprocess.check_output(['exit', '0'], shell=True)
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_output(['exit', '0'], shell=True) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_output(['exit', '0'], shell=True) has raised "+\
           "different exception"
else:
    print "\nsubprocess.check_output(['exit', '0'], shell=True) has returned :",\
          returncode


try:
    returncode = subprocess.check_output('exit 0', shell=True)
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_output('exit 0', shell=True) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
except:
    print "\nsubprocess.check_output('exit 0', shell=True) has raised "+\
          "different exception"
else:
    print "\nsubprocess.check_output('exit 0', shell=True) has returned :",\
          returncode
print ""


#===============================================================================
try:
    returncode = subprocess.check_output('ls pavan', shell=True,\
                                         stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_output('ls pavan', shell=True) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
    print "CMD: %s \nOUTPUT: %s" %(e.cmd, e.output)
except:
    print "\nsubprocess.check_output('ls pavan', shell=True) has raised "+\
          "different exception"
else:
    print "\nsubprocess.check_output('ls pavan', shell=True) has returned :",\
          returncode

try:
    returncode = subprocess.check_output(['ls', 'pavan'],\
                                         stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    print "\nsubprocess.check_output(['ls', 'pavan']) has raised "+\
          "subprocess.CalledProcessError exception with returncode ",\
          e.returncode
    print "CMD: %s \nOUTPUT: %s" %(e.cmd, e.output)
except:
    print "\nsubprocess.check_output(['ls', 'pavan']) has raised "+\
          "different exception"
else:
    print "\nsubprocess.check_output(['ls', 'pavan']) has returned :",\
          returncode
