import os
from re import sub
import shutil
from sys import stdout
import minecraft_launcher_lib
from subprocess import *
import subprocess
import eel
import json
import uuid
import pythonSide.appComponment.ModpackDownloader.mpDownloader as mpDownloader

from cryptography.fernet import Fernet
import time
import threading
from threading import *
from concurrent.futures import ThreadPoolExecutor as Pool
import logging

import crashreport

import linecache




e=None

@eel.expose
def getSelectVersion():
        user = os.getlogin()
        try:
            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                data = json.load(jsonFile)
                crack = data["crack"][0]["select"]
                microsoft = data["microsoft"][0]["select"]
                mojang = data["mojang"][0]["select"]

            if crack == "True":
                return "crack"
            elif microsoft == "True":
                return "microsoft"
            elif mojang == "True":
                return "mojang"
            else:
                print("please connects")
                eel.noc()
                return None
                

        except:
            print("please connect")
            eel.noc()
            return None

def callback(future):
    if future.exception() is not None:
        print("got exception: %s" % future.exception())
    else:
        print("process returned %d" % future.result())

def returnException():
    import sys
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    a = 'EXCEPTION IN (' + str(filename) + ' ::: LINE: ' + str(lineno) + str(line.strip()) +')::::' + str(exc_obj)
    return a
    
    

            
def execute_command(command):

    print("save of starting command !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")



    logging.basicConfig(
    level=logging.INFO,
    format=("%(relativeCreated)04d %(process)05d %(threadName)-10s "
            "%(levelname)-5s %(msg)s"))

    # wait for the process completion asynchronously
    print("begin waiting")
    pool = Pool(max_workers=1)
    f = pool.submit(subprocess.call, command, shell=False)
    f.add_done_callback(callback)
    pool.shutdown(wait=False)
    #subprocess.run(command)

    while True:
        if f.done() == True:
            eel.message("Minecraft process is finish !!. If it is a crash please lauch with command line mode to see the error.")
            break



    
    
     # no .submit() calls after that point
    print("continue waiting asynchronously")

    #subprocess.call(command)

    #import pickle

    #with open('command', 'wb') as fp:
        #pickle.dump(command, fp)

    #os.remove("launchingPart.txt")

    #subprocess.call("start.bat")

    
def ree():
    for i in range(50):
        print("test")
        time.sleep(0.5)

def execute_commands(command):
    print(command)
    eel.spawn(mino(command))

def ret(n):
    print(n)

def test():
    eel.returnInfo()(lambda n: ret(n))


def ok(pr):
    f = open("percent.txt", "w")
    f.write(str(pr))
    f.close()

def minecraft(n):

    try:

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

        xx = data["gameResolution"]["x"]

        y = data["gameResolution"]["y"]

        min = data["ram"]["min"]

        max = data["ram"]["max"]

        java = data["java"]
        version = n[1]
        motor = n[0]
        print("motor is : ", motor)
        login = getSelectVersion()
        print("the login methode is : ",login)

        if version == "alpha67" and login != None:
            directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
            print('start alpha laucher to connect to the server')
            user = os.getlogin()
            motor = "Forge"
            version = "1.16.5"

            def maximum(max_value, value):
                max_value[0] = value

            print('start minecraft for server connection')
            max_value = [0]

            def updateBar(value, maxValue):
                percent = 100 * int(value) / int(maxValue[0])
                print(int(percent))
                if percent <= 95:
                    ok(percent)
                eel.sleep(0.001)
                return percent

            callback = {
                "setStatus": lambda text: print(text),
                "setProgress": lambda value: updateBar(value, max_value),
                "setMax": lambda value: maximum(max_value, value)
            }

            #self.ui.download.show()
            #self.ui.play.hide()
            print(motor)
            mpDownloader.down()
            forge_version = "1.16.5"

            forge_version = minecraft_launcher_lib.forge.find_forge_version(version)



            print(forge_version)
            forge_version = "1.16.5-36.2.34"

            try:
                forgeLauch = forge_version.replace("-", "-forge-")
            except:
                print("forge version can be download or not exist")
                forgeLauch = None
            print(forgeLauch)

            # if you lauche minecraft vanilla
            if motor == "vanilla":
                minecraft_launcher_lib.install.install_minecraft_version(version, directory, callback=callback)

                print("game lauch")
                eel.gameLauch()()
                a = 100
                ok(a)

            forge_version = "1.16.5-36.2.34"

            # if you lauche ;inecrqft forge
            if motor == "Forge":
                if forge_version == "None":
                    print("version non disponible de forge")

                else:
                    def checkVersionDoawnload():
                        try:
                            directory_mod = 'C:/Users/'+user+'/AppData/Roaming\.alpha67/alpha/versions'
                            files = os.listdir(directory_mod)
                            for f in files:
                                print("file: " + f)
                                if forgeLauch == f:
                                    print("version already download lauching minecraft")
                                    return True
                        except:
                            None

                    if checkVersionDoawnload() == None:

                        print("doawnloading:" + forgeLauch)
                        minecraft_launcher_lib.forge.install_forge_version(forge_version, directory, callback=callback)
                        print(forgeLauch)


            #self.ui.play.show()
            #self.ui.download.hide()

            login = getSelectVersion()
            print("the login methode is : ",login)
            ok("1000")

            ###########
            if login == "mojang":
                print("okok")
                with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'r') as file:
                    uInfo = json.load(file)
                    print(uInfo)
                    # uInfo = literal_eval(uInfo)

                    uInfo = uInfo['mojang']
                    uInfo = uInfo[0]
                    username = uInfo['username']
                    password = uInfo['password']
                    key = uInfo['key']
                fernet = Fernet(key)

                passwordEnc = str(user + "67")
                print(type(password))
                password = password.replace("'", '')
                password = password[1:]
                print("info ###################################")
                print(password)
                username = username.replace("'", '')
                username = username[1:]
                print(fernet)
                print(username)
                print("info #####################################")

                username = str.encode(username)
                password = str.encode(password)
                

                us = fernet.decrypt(username).decode()
                pa = fernet.decrypt(password).decode()

                print("the username decrypt is ", us)

                login_data = minecraft_launcher_lib.account.login_user(us, pa)
                print(login_data)
                options = {
                    "username": login_data["selectedProfile"]["name"],
                    "uuid": login_data["selectedProfile"]["id"],
                    "token": login_data["accessToken"],
                    "jvmArguments": ["-Xmx"+max+"m", "-Xms"+min+"m"],
                    "server": "alpha67.duckdns.org",
                    "port": "32451"

                }

                if motor == "vanilla":
                    minecraft_directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/'
                    command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                    options)
                    execute_command(command)
                elif motor == "Forge":
                    print("crack, lauching minecraft, version:" + forgeLauch)
                    directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                        forgeLauch, directory, options)

                    execute_command(minecraft_command)

            #################################################################################################
            if login == "microsoft":
                print("okok")
                with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/ACI.json', 'r') as file:
                    uInfo = json.load(file)
                    print(uInfo)
                    # uInfo = literal_eval(uInfo)
                options = {
                    "username": uInfo["name"],
                    "uuid": uInfo["id"],
                    "token": uInfo["access_token"],
                    "jvmArguments": ["-Xmx"+max+"m", "-Xms"+min+"m"],
                    "server": "alpha67.duckdns.org",
                    "port": "32451"
                }

                if motor == "vanilla":
                    minecraft_directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/'
                    command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                    options)
                    execute_command(command)
                elif motor == "Forge":
                    print("crack, lauching minecraft, version:" + forgeLauch)
                    directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                        forgeLauch, directory, options)

                    execute_command(minecraft_command)

            #########################################################################################################
            if login == "crack":
                print("okoksss")
                ma = "-Xmx"+max+"m"
                mi = "-Xms"+min+"m"
                with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'r') as file:
                    uInfo = json.load(file)
                    print(uInfo)
                    uInfo = uInfo['crack']
                    uInfo = uInfo[0]
                    username = uInfo['username']
                    # uInfo = literal_eval(uInfo)
                options = {
                    "username": username,
                    "uuid": uuid.uuid4().hex,
                    "token": "",
                    "jvmArguments": [ma, mi],
                    "server": "alpha67.duckdns.org",
                    "port": "32451"
                }

                print(forge_version)
                print(motor)
                if motor == "vanilla":
                    minecraft_directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/'
                    command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                    options)
                    execute_command(command)
                elif motor == "Forge":
                    try:
                        print("crack, lauching minecraft, version:" + forgeLauch)
                        directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                            forgeLauch, directory, options)
                        print(minecraft_command)

                        execute_command(minecraft_command)
                    except:
                        None

        elif(login != None):

            version = n[1]

            forge_version = minecraft_launcher_lib.forge.find_forge_version(version)

            try:
                forgeLauch = forge_version.replace("-", "-forge-")
                print(forgeLauch)
            except Exception as e: 
                print(e)
            
            motor = n[0]
            user = os.getlogin()
            def maximum(max_value, value):
                max_value[0] = value

            print('start minecraft')
            max_value = [0]

            #@eel.expose
            def installVersion(needReinstall):

                version = n[1]
            
                motor = n[0]
                user = os.getlogin()
                def maximum(max_value, value):
                    max_value[0] = value

                print('start minecraft')
                max_value = [0]

                def updateBarf(value, maxValue):
                    percent = 100 * int(value) / int(maxValue[0])
                    ok(percent)
                    eel.sleep(0.001)
                    return percent
                    #self.ui.download.setValue(percent)

                def callbackInfo(text):
                    if text.isdigit():
                        print("oksss")
                        return None
                        
                    else:
                        print("ok")
                        return text

                callback = {
                    "setStatus": lambda text: callbackInfo(text),
                    "setProgress": lambda value: updateBarf(value, max_value),
                    "setMax": lambda value: maximum(max_value, value)
                }


                #self.ui.download.show()
                #self.ui.play.hide()
                
                

                #if you lauche minecraft vanilla
                print("the motor is : ",motor)
                if motor == "vanilla":
                    print("dowload of minecraft vanilla : ",version)
                    directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/'

                    def checkVersionDoawnload():
                        try:
                            directory_mod = 'C:/Users/'+user+'\AppData\Roaming\.alpha67\minecraft/versions'
                            files = os.listdir(directory_mod)
                            for f in files:
                                print("file: "+f)
                                if version == f:
                                    print("version already download lauching minecraft")
                                    return True
                                    break
                        except:
                            print("cannot install version:", version)
                            return None

                    if checkVersionDoawnload() == None or needReinstall == True:
                        
                        try:
                            print("doawnloading:",version)
                            directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/'
                            try:
                                shutil.rmtree('C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/versions/'+version)
                            except:
                                print("no directory: "+ version)

                            minecraft_launcher_lib.install.install_minecraft_version(version, directory, callback=callback)

                            print("update version json file")

                            with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/version.json', 'r') as file:
                                data = json.load(file)

                            with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/version.json', 'w') as file:
                                x = {"version": version}
                                data.update(x)

                                print(data)

                                json.dump(data, file)

                            #return uInfo

                            a = 100
                            ok(a)

                            if needReinstall == True:
                                lauchGame()

                        except Exception as e: 
                            with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/version.json', 'w') as file:
                                print("update firste line version json.")
                                x = {"version": version}
                                json.dump(x, file)
                            print(repr(e))


                    
                    a = 128
                    ok(a)

                #if you lauche ;inecrqft forge
                if motor == "forge":
                    if forge_version == "None":
                        print("version non disponible de forge")

                    else:
                        def checkVersionDoawnload():
                            try:
                                directory_mod = 'C:/Users/'+user+'\AppData\Roaming\.alpha67\minecraft/versions'
                                files = os.listdir(directory_mod)
                                for f in files:
                                    print("file: "+f)
                                    if forgeLauch == f:
                                        print("version already download lauching minecraft")
                                        return True
                                        break
                            except:
                                print("version note found starting his installation.")
                                return None

                        if checkVersionDoawnload() == None or needReinstall == True:

                            print("doawnloading:"+forgeLauch)
                            directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/'
                            try:
                                shutil.rmtree('C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/versions/'+forge_version)
                            except:
                                print("no directory"+forge_version)
                            minecraft_launcher_lib.forge.install_forge_version(forge_version, directory,
                                                                                callback=callback)

                            print(forgeLauch)
                            a = 100
                            ok(a)

                            if needReinstall == True:
                                lauchGame()

                            

            installVersion(False)
            #self.ui.play.show()
            #self.ui.download.hide()

            def lauchGame():
                print("pppppppppppppppppppppp"+login+motor)
                ###########
                if login == "mojang":
                    print("okok")
                    with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'r') as file:
                        uInfo = json.load(file)
                        print(uInfo)
                        # uInfo = literal_eval(uInfo)

                        uInfo = uInfo['mojang']
                        uInfo = uInfo[0]
                        username = uInfo['username']
                        password = uInfo['password']
                        key = uInfo['key']

                    fernet = Fernet(key)

                    passwordEnc = str(user + "67")
                    print(type(password))
                    password = password.replace("'", '')
                    password = password[1:]
                    print("info ###################################")
                    print(password)
                    username = username.replace("'", '')
                    username = username[1:]
                    print(fernet)
                    print(username)
                    print("info #####################################")

                    username = str.encode(username)
                    password = str.encode(password)
                    

                    us = fernet.decrypt(username).decode()
                    pa = fernet.decrypt(password).decode()

                    login_data = minecraft_launcher_lib.account.login_user(us, pa)

                    print(login_data)
                    options = {
                        "username": login_data["selectedProfile"]["name"],
                        "uuid": login_data["selectedProfile"]["id"],
                        "token": login_data["accessToken"],
                        "jvmArguments": ["-Xmx"+max+"m", "-Xms"+min+"m"]
                    }
                    #crashreport.inject_excepthook(lambda etype, value, tb, dest: print('Dumped crash report to', dest))

                    if motor == "vanilla":
                        minecraft_directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/'
                        command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                        options)
                        execute_command(command)
                    elif motor == "forge":
                        print("crack, lauching minecraft, version:"+forgeLauch)
                        directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/'
                        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                            forgeLauch, directory, options)

                        execute_command(minecraft_command)


                #################################################################################################
                if login == "microsoft":
                    print("okok")
                    with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/ACI.json', 'r') as file:
                        uInfo = json.load(file)
                        print(uInfo)
                        # uInfo = literal_eval(uInfo)
                    options = {
                        "username": uInfo["name"],
                        "uuid": uInfo["id"],
                        "token": uInfo["access_token"],
                        "jvmArguments": ["-Xmx"+max+"m", "-Xms"+min+"m"]
                    }

                    if motor == "vanilla":
                        minecraft_directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/'
                        command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                        options)
                        execute_command(command)
                    elif motor == "Forge":
                        print("crack, lauching minecraft, version:"+forgeLauch)
                        directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/'
                        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                            forgeLauch, directory, options)

                        execute_command(minecraft_command)

                #########################################################################################################
                if login == "crack":
                    print("okoksss")
                    with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'r') as file:
                        uInfo = json.load(file)
                        print(uInfo)
                        uInfo = uInfo['crack']
                        uInfo = uInfo[0]
                        username = uInfo['username']
                        # uInfo = literal_eval(uInfo)
                    options = {
                        "username": username,
                        "uuid": uuid.uuid4().hex,
                        "token": "",
                        "jvmArguments": ["-Xmx"+max+"m", "-Xms"+min+"m"],
                        "launcherName": "PyMyMC"
                    }
                    try:
                        print(forge_version)
                    except:
                        None
                    print(motor)
                    if motor == "vanilla":
                        minecraft_directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/'
                        try:
                            command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)
                            print(command)
                            execute_command(command)
                        except:
                            print("can't lauch the game, starting reinstall of the version")
                            eel.alertP("can't lauch the game, starting reinstall of the version")
                            installVersion(True)


                        
                    elif motor == "forge":

                        directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/minecraft/'
                        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(forgeLauch, directory, options)
                        print(minecraft_command)
                        print("execute command pour crack forge pas alpha")
                        execute_command(minecraft_command)

            lauchGame()

            def maximum(max_value, value):
                max_value[0] = value

    except:
        print("-------------------ERROR----------------------")
        import traceback
        print(traceback.format_exc())
        print("-------------------ERROR----------------------")
        eel.alertP(returnException())
        #print(PrintException)
        





    

def start(n):
    print(n)
    f = open("demofile2.txt", "w")
    f.write(str(n))
    f.close()


def lauch():
    l = open("launchingPart.txt","w")
    l.write("yes")
    l.close
    try:
        eel.returnInfo()(lambda n: minecraft(n))
    except:
        eel.alertP("salut")
