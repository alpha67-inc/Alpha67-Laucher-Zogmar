import subprocess
import pickle
import os 

with open ('command', 'rb') as fp:
    command = pickle.load(fp)

print(type(command))

subprocess.call(command)

#os.remove('command')
