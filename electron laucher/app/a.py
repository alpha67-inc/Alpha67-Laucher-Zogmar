import eel
import random
import os
import minecraft_launcher_lib
import requests
import subprocess
import json
import uuid
#import pythonSide.appComponment.ModpackDownloader.mpDownloader as mpDownloader


def javaEx(what):

    user = os.getlogin()
    settings = 'C:/Users/'+user+'/AppData/Roaming\.alpha67/alpha/settings.json'

    with open(settings, 'r') as s:
    	data = json.load(s)
    	print(type(data))
    


    if what == "GRX":
        data = data["gameResolution"]
        print(data)
        return data

print(javaEx("GRX"))