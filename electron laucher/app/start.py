import subprocess
import pickle
import os 
import time



with open ('command', 'rb') as fp:
    command = pickle.load(fp)

print(type(command))

subprocess.call(command)

time.sleep(10)



#os.remove('command')
