#this ,is a simple script to run another Python script multiple times
# It uses the subprocess module to call the script
# Import the subprocess module to run external commands
# this module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes
#this module allows python to connect with CLI and run commands
#this module allows you to run a script from another script

import subprocess

for i in range(5):
    subprocess.check_call(["python", "example.py"])