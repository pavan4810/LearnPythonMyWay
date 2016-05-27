"""
Notes: =========================================================================
NNotes:  subprocess.check_call(args, *, stdin=None, stdout=None,
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
Notes:          subprocess.call([arg1, arg2, ...])
otes:
Notes:
Notes:
"""

import subprocess

# Command with space, need shell=True
print "Output from : ", "subprocess.check_call('ls -l', shell=True)"
print "Return code ", subprocess.check_call("ls -l", shell=True)

print "Output from : ", "subprocess.check_call(['ls', '-l'])"
print "Return code ", subprocess.check_call(['ls', '-l'])

print subprocess.check_call("ls -l")
print subprocess.check_call("ls -l".split())
print subprocess.check_call("exit 9", shell=True)

#print subprocess.check_output(['bash', '-c', 'ls -l'])
#count = subprocess.check_output(['bash', '-c', 'ls -l | wc -l'])
#print "Count = ", count
#

#try:
#    subprocess.check_call("exit 9", shell=True)
#except subprocess.CalledProcessError as p:
#    print "Exited with code", p.returncode
#    print "Exited with code", subprocess.call("exit 9", shell=True)

#p = subprocess.Popen(['ls', '-l'])
#(output, error) = p.communicate()
#print output

#output = subprocess.check_output(['bash', '-c', 'ls /proc/*/pavan 2> /dev/null | wc -l'])
#if int(output) > 0:
#    for line in output.splitlines():
#      print "Line: ", line

#p = subprocess.Popen(['bash', '-c', 'ls /proc/*/maps'], stdout=subprocess.PIPE)
#(output, error) = p.communicate()
#print type(output), type(error)
#for line in (output):
#  print "Output: ", line
#for line in (error):
#  print "Error: ", line

#command = "ls -l"
#output = subprocess.call(command.split(), shell=True)
#print type(output)
#
#output = subprocess.call(command.split(), shell=False)
#print type(output)

#command = "ls /proc/*/maps"
#command = "exit 2"
#p = subprocess.Popen(["bash", "-c", command],
#                     stdout=subprocess.PIPE,
#                     stderr=subprocess.PIPE)
#print "Pid = ", p.pid, "Return code = ", p.returncode
#(output, error) = p.communicate()
#for line in output.splitlines():
#  print "O/P: ", line
#for line in error.splitlines():
#  print "Error: ", line

#command = "ls /proc/*/maps"
#command = "ls"
#p = subprocess.Popen(["bash", "-c", command],
#                     stdout=subprocess.PIPE,
#                     stderr=subprocess.PIPE)
#print "Pid = ", p.pid, "Return code = ", p.returncode
#while True:
#    char = p.stdout.read(1)
#    print char,
