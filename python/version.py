import os
import subprocess

process = subprocess.Popen(['git','branch'], stdout=subprocess.PIPE)
output = process.communicate()

print output
