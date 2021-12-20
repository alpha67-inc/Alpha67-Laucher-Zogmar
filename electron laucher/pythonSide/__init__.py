import os
import minecraft_launcher_lib
import requests
 
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

def get_library_version() -> str:
    return "4.0"

def getVersions():
    vlist = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json", headers={"user-agent": f"minecraft-launcher-lib/{get_library_version()}"}).json()
    returnlist = []
    for i in vlist["versions"]:
        returnlist.append({"id": i["id"], "type": i["type"]})
    return returnlist


