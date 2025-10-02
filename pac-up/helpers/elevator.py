import os
import sys
import subprocess

# Helper to be called in other parts of the program to elevate permissions
def elevate(ex, is_python_script: bool , args=None):
    if args is None:
        args = []

    try:
        if is_python_script:
            return subprocess.run(['/usr/bin/pkexec', sys.executable , os.getcwd()+"/"+ex] + args, check=True, stdout=subprocess.PIPE)
        elif not is_python_script:
            return subprocess.run(['/usr/bin/pkexec', ex] + args, check=True, stdout=subprocess.PIPE)
    except Exception as e:
        return e