import json
import urllib.request
import time
import os
import shutil
from colorama import Fore, Back, Style
from datetime import date, datetime
from ast import literal_eval
import tkinter
from tkinter import filedialog
#from win10toast_click import ToastNotifier

import sys
import pythonSide.appComponment.ModpackDownloader.version as version

def down():
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

    user = os.getlogin()
    MYDIR = "C:/Users/" + user + "/AppData/Roaming/.alpha67/alpha/mods"
    CHECK_FOLDER = os.path.isdir(MYDIR)
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)
        createDirectory("mods", "C:/Users/" + user + "/AppData/Roaming/.alpha67/alpha/")


    def get():
        print(Back.WHITE + Fore.BLACK + "SVP veuillez renseigner où est votre dossier mods minecraft.")
        tkinter.Tk().withdraw()
        user = os.getlogin()
        folder_path = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/mods'
        #folder_path = dirName = filedialog.askdirectory(initialdir="C:/Users/" + user + "/AppData/Roaming/.minecraft",
        #                                               title='Please select a directory')
        return folder_path


    def createDirectory(name, parent):
        path = parent + "/" + name
        isdir = os.path.isdir(path)
        if isdir == False:
            directory = name
            parent_dir = parent
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            print("Directory '% s' created" % directory)


    MYDIR = "C:/Users/" + user + "/alpha67_MP"
    CHECK_FOLDER = os.path.isdir(MYDIR)
    adress = get()
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)
        createDirectory("alpha67_MP", "C:/Users/" + user)
        createDirectory("mods", "C:/Users/" + user + "/alpha67_MP")
        update = True
        adress = get()
        needGetJsonAdress = False

    else:
        update = version.needUpdate()
        needGetJsonAdress = True

    if update == True:

        infoFile = 'C:/Users/' + user + '/alpha67_MP/data.json'

        if needGetJsonAdress == True:
            with open(infoFile, 'r') as file:
                uInfo = json.load(file)
                uInfo = literal_eval(uInfo)

        for files in os.listdir(adress):
            if os.path.isfile(os.path.join(adress, files)):
                print(files)
                print(adress)
                os.remove(adress + '/' + files)

        try:
            None
        except:
            print("sorry but the program can't connect to internet")
        response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/desktop-tutorial/releases")
        data = json.loads(response.read())
        data = data[0]
        data = data["assets"]
        data = data[0]
        url = data["browser_download_url"]

        print(Back.WHITE + Fore.BLACK + "Nous allons installer les mods dans ce repèrtoir : " + adress)
        time.sleep(1)
        print(Back.BLACK + Fore.WHITE + "connection au server")
        time.sleep(0.5)
        print(Fore.WHITE + """    using System.Data.SqlClient;
    
            var conn = new SqlConnection();
            conn.ConnectionString = 
                          "Data Source=git.677;" + 
                          "Initial Catalog=duckdns.org;" + 
                          "Integrated Security=SSPI;"; 
            conn.Open();""")
        time.sleep(0.4)
        print("démarrage du téléchargement...")

        user = os.getlogin()

        path = "C:/Users/" + user + "/alpha67_MP/mods/mp.zip"


        def cbk(a,b,c):  

            '''''Callback function 
            @a:Downloaded data block 
            @b:Block size 
            @c:Size of the remote file 
            '''  
            per=100.0*a*b/c  
            if per>100:  
                per=100 

            

            
            print (per, a, b, c) 

            tex = "telechargement du laucher : "+str(int(per))+"% "
            
            #self.canvas.itemconfig(self.info, text=tex)

        urllib.request.urlretrieve(url, path, cbk)
        
        with ZipFile(path, 'r') as zip:
            zip.printdir()
            zip.extractall(adress)






        urllib.request.urlretrieve(url, "C:/Users/" + user + "/alpha67_MP/mods/mp.zip")

        original = r'C:/Users/' + user + '/alpha67_MP/mp.zip'
        target = adress + "/ModPack.zip"

        # shutil.copyfile(original, target)

        from zipfile import ZipFile

        with ZipFile('C:/Users/' + user + '/alpha67_MP/mods/mp.zip', 'r') as zip:
            zip.printdir()
            zip.extractall(adress)

        user = os.getlogin()
        data = """{ok: salut}"""
        response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/desktop-tutorial/releases")
        data = json.loads(response.read())
        data = data[0]
        data = data["tag_name"]
        print(data)

        da = date.today()
        now = datetime.now()
        print(da)

        with open('C:/Users/' + user + '/alpha67_MP/ListMods.txt', 'w') as f:
            f.write('')

        with open('C:/Users/' + user + '/alpha67_MP/ListMods.txt', 'a') as f:
            for files in os.listdir(adress):
                if os.path.isfile(os.path.join(adress, files)):
                    print(files)
                    f.write(files + "\n")

        with open('C:/Users/' + user + '/alpha67_MP/data.json', 'w') as outfile:
            json.dump(str({"time": str(now), "version": data, "path": adress}), outfile)

        for i in range(100):
            print(Fore.GREEN + "unziping file " + str(i) + "%, directory get")
            time.sleep(0.005)

        with open('C:/Users/' + user + '/alpha67_MP/listMod.txt', 'w') as f:
            f.write('')
        me = ""
        with open('C:/Users/' + user + '/alpha67_MP/listMod.txt', 'a') as f:
            for files in os.listdir(adress):
                if os.path.isfile(os.path.join(adress, files)):
                    f.write(files)
                    print(files)
                    me = me + "[ " + files + " ]"
                    me = me

        x = me.split(" ")

        print(":::::Le modpack est correctement installer.")




    else:
        # initialize
        print("mp is up to date!")
