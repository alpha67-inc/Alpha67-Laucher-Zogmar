import os
import minecraft_launcher_lib
import requests
import os
import eel
from pythonSide.appComponment.mojang import *
from pythonSide.appComponment.crack import *
from pythonSide.appComponment.start import *
 
 #creation de fichier si il ne sont pas créée
def start():
    def createDirectory(name, parent):
        path = parent + "/" + name
        isdir = os.path.isdir(path)
        if isdir == False:
            directory = name
            parent_dir = parent
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            print("Directory '% s' created" % directory)

    user = os.getlogin()
    MYDIR = "C:/Users/" + user + "/AppData/Roaming/.alpha67"
    CHECK_FOLDER = os.path.isdir(MYDIR)
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)
        createDirectory(".alpha67", "C:/Users/" + user + "/AppData/Roaming/")
    MYDIR = "C:/Users/" + user + "\AppData\Roaming\.alpha67/minecraft"
    CHECK_FOLDER = os.path.isdir(MYDIR)
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)
        createDirectory("minecraft", "C:/Users/" + user + "\AppData\Roaming\.alpha67/")
    MYDIR = "C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha"
    CHECK_FOLDER = os.path.isdir(MYDIR)
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)
        createDirectory("alpha", "C:/Users/" + user + "\AppData\Roaming\.alpha67/")
    try:
        with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
            data = json.load(jsonFile)
            print(data)
    except:
        x = {

        "mojang": [
            {"connect": "False", "select": "False"}
        ],
        "microsoft": [
            {"connect": "False", "select": "False"}
        ],
        "crack": [
            {"connect": "False", "select": "False"}
        ]
            }

        with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "w") as jsonFile:
                json.dump(x,jsonFile)

def get_library_version() -> str:
    return "4.0"

def getVersions():
    vlist = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json", headers={"user-agent": f"minecraft-launcher-lib/{get_library_version()}"}).json()
    returnlist = []
    for i in vlist["versions"]:
        returnlist.append({"id": i["id"], "type": i["type"]})
    return returnlist

@eel.expose
def startMicrosoft():
    print(os.getcwd())
    os.startfile('microsoftLogin.exe')

@eel.expose
def startMojangLogin():
    upass()

@eel.expose
def startCrackLogin():
    crack()

@eel.expose
def StartMinecraft():
    lauch()

@eel.expose
def isUseC():
    try:
        file1 = open("launchingPart.txt","r+") 
        i = file1.read()
        print(i)

        if i == "yes":
            print("yes")
            None
        else:
            print("ok")
            print("in process")
            eel.sett2()()
    
    except:
        print("ok")
        print("in process")
        eel.sett2()()

@eel.expose
def isUseS():
    try:
        file1 = open("launchingPart.txt","r+") 
        i = file1.read()

        if i == "yes":
            None
        else:
            print("ok")
            print("in process")
            eel.sett()()
    
    except:
        print("ok")
        print("in process")
        eel.sett()()

@eel.expose
def read():

    f = open("percent.txt", "r")
    value = f.read()
    value = float(value)
    print(value)
    return value

@eel.expose
def javaEx(what):

    user = os.getlogin()
    settings = 'C:/Users/'+user+'/AppData/Roaming\.alpha67/alpha/settings.json'

    try:
        with open(settings, 'r') as s:
            data = json.load(s)
    
    except:

        print("error")

        defaultSett = {

                "gameResolution": 
                    {
                        "x": "auto",
                        "y": "auto"
                    },

                "ram": {
                    "min": "1000",
                    "max": "3000"
                },

                "java": "auto"
            }

        with open(settings, 'w') as outfile:
            json.dump(defaultSett, outfile)

        data = defaultSett

    if what == "GRX":
        data = data["gameResolution"]["x"]
        print(data)
        return data

    if what == "GRY":
        data = data["gameResolution"]["y"]
        print(data)
        return data

    if what == "RAMMIN":
        data = data["ram"]["min"]
        print(data)
        return data
    
    if what == "RAMMAX":
        data = data["ram"]["max"]
        print(data)
        return data

    if what == "JAVA":
        data = data["java"]
        print(data)
        return data


@eel.expose
def saveSettings(x,y,min,max,java):

    user = os.getlogin()
    settings = 'C:/Users/'+user+'/AppData/Roaming\.alpha67/alpha/settings.json'

    sett = {

        "gameResolution": 
            {
                "x": x,
                "y": y
            },

        "ram": {
            "min": min,
            "max": max
        },

        "java": java
    }

    with open(settings, 'w') as outfile:
            json.dump(sett, outfile)