import re
import json
import urllib
import urllib.request
import time
import tkinter
from tkinter import filedialog
import os
import os.path
import shutil
from colorama import Fore, Back, Style
from datetime import date, datetime
from ast import literal_eval

user = os.getlogin()

def createDirectory(name, parent):
    path = parent + "/" + name
    isdir = os.path.isdir(path)
    if isdir == False:
        directory = name
        parent_dir = parent
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        print("Directory '% s' created" % directory)


def needUpdate():
    def needUpdateJson():
        user = os.getlogin()
        data = """{ok: salut}"""
        response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/desktop-tutorial/releases")
        data = json.loads(response.read())
        data = data[0]
        data = data["tag_name"]

        da = date.today()
        now = datetime.now()

        try:
            f = open('C:/Users/' + user + '/alpha67_MP/data.json')

            print("File data is already create.")
            time.sleep(0.5)
            print("checking the current version.")

            with open('C:/Users/' + user + '/alpha67_MP/data.json', 'r') as json_file:
                uInfo = json.load(json_file)
                uInfo = literal_eval(uInfo)
                uInfo = uInfo["version"]

            if uInfo != data:
                return True
            else:
                return False
            # Do something with the file
        except IOError:
            with open('C:/Users/' + user + '/alpha67_MP/data.json', 'w') as outfile:
                json.dump(str({"time": str(now), "version": None}), outfile)
            print("File not accessible, starting his creation")
            return True


    def needUpdateJar():

        try:

            i = 0
            ok = ""

            infoFile = 'C:/Users/' + user + '/alpha67_MP/data.json'

            try:
                with open(infoFile, 'r') as file:
                    uInfo = json.load(file)
                    uInfo = literal_eval(uInfo)
                    path = uInfo['path']
            except:
                return True


            def existFile():
                try:
                    open('C:/Users/' + user + '/alpha67_MP/listMod.txt', 'r')
                    return True
                except:

                    return False

            if existFile() == False:
                f = open('C:/Users/' + user + '/alpha67_MP/listMod.txt', 'w+')


            with open('C:/Users/' + user + '/alpha67_MP/listMod.txt', 'a') as f:
                for files in os.listdir(path):
                    if os.path.isfile(os.path.join(path, files)):
                        i = i+1
                        ok = ok + files
                        f.write(files)
                if i == 0:
                    return True
                else:
                    with open('C:/Users/' + user + '/alpha67_MP/listMod.txt') as f:
                        contents = f.readlines()
                    print(contents)
                    with open('C:/Users/' + user + '/alpha67_MP/listMod.txt', 'w') as f:
                        f.write('')
                        # print(contents)


            contents = contents[0]

            if contents == ok:
                return False
            else:
                return True
        except:
            return True

    jsonU = needUpdateJson()
    jar = needUpdateJar()

    if jar == True:
        print("jar is modified")
    if jsonU == True:
        print("json version not up to date.")

    if jar or jsonU == True:
        print("need update")
        return True
