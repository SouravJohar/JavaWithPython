import sys
import os.path,subprocess
from subprocess import STDOUT,PIPE

def compile_java(java_file):
    subprocess.check_call(['javac', java_file])
def execute_java(java_file, parameterlist):
     cmd = ['java', java_file] + parameterlist
     proc = subprocess.Popen(cmd, stdout=PIPE, stderr = STDOUT)
     stdout,stderr = proc.communicate()
     return stdout

parameters = []
for i in range(len(sys.argv)):
    if i == 0:
        continue
    else:
        parameters.append(sys.argv[i])

compile_java('JavaModule.java')
output = execute_java('JavaModule', parameters).split(" ")
for item in output:
    if item != "":
        print item
