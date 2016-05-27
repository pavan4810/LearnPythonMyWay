"""
Notes: =========================================================================
Notes:
Notes:
Notes:
"""

import subprocess

#print subprocess.check_output(['bash', '-c', 'ls -l'])
#count = subprocess.check_output(['bash', '-c', 'ls -l | wc -l'])
#print "Count = ", count
#
#print subprocess.call("ls -l".split())
#print subprocess.call("exit 9", shell=True)

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
