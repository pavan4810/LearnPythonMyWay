"""
Notes: =========================================================================
Notes: class subprocess.Popen(args,
Notes:                        bufsize=0,
Notes:                        executable=None,
Notes:                        stdin=None,
Notes:                        stdout=None,
Notes:                        stderr=None,
Notes:                        preexec_fn=None,
Notes:                        close_fds=False,
Notes:                        shell=False,
Notes:                        cwd=None,
Notes:                        env=None,
Notes:                        universal_newlines=False,
Notes:                        startupinfo=None,
Notes:                        creationflags=0)
Notes:
Notes:      If preexec_fn is set to a callable object, this object will be
Notes:      called in the child process just before the child is executed.
Notes:
Notes:      If close_fds is true, all file descriptors except 0, 1 and 2
Notes:      will be closed before the child process is executed.
Notes:
Notes:      If cwd is not None, the child's current directory will be changed to
Notes:      cwd before it is executed.
Notes:
Notes:      If env is not None, it must be a mapping that defines the
Notes:      environment variables for the new process;
Notes:
Notes:      If universal_newlines is True, the file objects stdout and stderr
Notes:      are opened as text files in universal newlines mode. Lines may be
Notes:      terminated by any of '\n', the Unix end-of-line convention,
Notes:                           '\r', the old Macintosh convention or
Notes:                           '\r\n', the Windows convention. All of these
Notes:      external representations are seen as '\n' by the Python program.
Notes:
Notes:      If given, startupinfo will be a STARTUPINFO object, which is passed
Notes:      to the underlying CreateProcess function.
Notes:      creationflags, if given, can be CREATE_NEW_CONSOLE
Notes:
Notes:
Notes:  Popen Objects:
Notes:  Popen.poll()
Notes:      Check if child process has terminated.
Notes:      Set and return returncode attribute.
Notes:
Notes:  Popen.wait()
Notes:      Wait for child process to terminate.
Notes:      Set and return returncode attribute.
Notes:
Notes:  Popen.communicate(input=None) interact with process:
Notes:      Send data to stdin.
Notes:      Read data from stdout and stderr, until end-of-file is reached.
Notes:      Wait for process to terminate.
Notes:      The optional input argument should be a string to be sent to
Notes:      the child process, or None, if no data should be sent to the child.
Notes:      
Notes:      communicate() returns a tuple (stdoutdata, stderrdata).
Notes:      
Notes:      Note that if you want to send data to the process's stdin,
Notes:      you need to create the Popen object with stdin=PIPE.
Notes:      Similarly, to get anything other than None in the result tuple,
Notes:      you need to give stdout=PIPE and/or stderr=PIPE too.
Notes:
Notes:  Popen.send_signal(signal)
Notes:  Popen.terminate()   - SIGTERM
Notes:  Popen.kill()        - SIGKILL
Notes:
Notes:  Popen.stdin
Notes:      If the stdin argument was PIPE, this attribute is a file object
Notes:      that provides input to the child process. Otherwise, it is None.
Notes:  Popen.stdout
Notes:      If the stdout argument was PIPE, this attribute is a file object
Notes:      that provides output from the child process. Otherwise, it is None.
Notes:  Popen.stderr
Notes:      If the stderr argument was PIPE, this attribute is a file object
Notes:      that provides error from the child process. Otherwise, it is None.
Notes:
Notes:  Popen.pid
Notes:      The process ID of the child process.
Notes:
Notes:  Popen.returncode
Notes:      The child return code, set by poll() and wait() (and indirectly
Notes:      by communicate()).
Notes:      A None value indicates that the process hasn't terminated yet.
Notes:      A negative value -N indicates that the child was terminated by
Notes:      signal N.
Notes:
Notes:
"""

import subprocess

#===============================================================================
# As stdout and stderr arguments are absent,
# (output, error) will be of type None.
#===============================================================================
p = subprocess.Popen(['ls', '-l'])
(output, error) = p.communicate()
print type(output), type(error)
print "\n"



#===============================================================================
# As stdout and stderr arguments are subprocess.PIPE,
# (output, error) will be of type str.
#===============================================================================
p = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(output, error) = p.communicate()
print type(output), type(error)
print "Output1      : ", output.strip('\r\n')
print "error1       : ", error.strip('\r\n') 
print "Return code1 : ", p.poll()
print "\n"



#===============================================================================
# As stdout and stderr arguments are subprocess.PIPE,
# (output, error) will be of type str.
# p.poll can be used to return returncode if child has terminated.
#===============================================================================
p = subprocess.Popen(['ls', '-l', 'pavan'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(output, error) = p.communicate()
print "Output2      : ", output.strip('\r\n')
print "error2       : ", error.strip('\r\n')
print "Pid          : ", p.pid
print "Return code2 : ", p.poll()
print "Return code2 : ", p.returncode
print "\n"


#===============================================================================
#
#===============================================================================
output = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE).communicate()[0]
if output:
    for line in output.splitlines():
      print "O/P: ", line
print "\n"



#===============================================================================
# using bash
#===============================================================================
command = "ls /proc/*/maps | wc -l"
p = subprocess.Popen(["bash", "-c", command],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
(output, error) = p.communicate()
if output:
    for line in output.splitlines():
      print "O/P: ", line
else:
    print "No output"
print "\n"



#===============================================================================
# Using bash.
# Using p.stdout
#===============================================================================
command = "ls /proc/*/maps | head"
p = subprocess.Popen(["bash", "-c", command],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
data = p.stdout.readlines()
if output:
    for line in data:
        print "O/P: ", line.strip('\r\n')
else:
    print "No output"
