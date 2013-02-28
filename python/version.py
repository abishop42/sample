import os
import subprocess

process = subprocess.Popen(['git','branch'], stdout=subprocess.PIPE)
print process.stdout
