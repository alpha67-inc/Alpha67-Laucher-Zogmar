import os
import minecraft_launcher_lib
import subprocess
import eel
import json
import uuid

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

        except:
            print("please connect")


def execute_command(command):
        # QProcess.start takes as first argument the program and as second the list of arguments
        # So we need the filter the program from the command
        arguments = command[1:]
        # Deactivate the launch button
        #self.launch_button.setEnabled(False)
        # Clear the text  field
        #self.setPlainText("")
        process = QProcess(self)
        # Activate the launch button when Minecraft is closed
        #self.process.finished.connect(lambda: self.play.setEnabled(True))
        # Connect the function to display the output
        #self.process.readyRead.connect(self.dataReady)
        # Start Minecraft
        process.start("java", arguments)

def start(n):
    user = os.getlogin()

    def maximum(max_value, value):
        max_value[0] = value

    version = n[1]
    motor = n[0]

    if version == "alpha67":
        directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
        print('start alpha laucher to connect to the server')
        user = os.getlogin()
        motor = "Forge"
        version = "1.16.5"

        def maximum(max_value, value):
            max_value[0] = value

        print('start minecraft')
        max_value = [0]

        def updateBar(value, maxValue):
            percent = 100 * int(value) / int(maxValue[0])
            # print(int(percent))
            #self.ui.download.setValue(percent)

        callback = {
            "setStatus": lambda text: print(text),
            "setProgress": lambda value: updateBar(value, max_value),
            "setMax": lambda value: maximum(max_value, value)
        }

        #self.ui.download.show()
        #self.ui.play.hide()
        print(motor)
        forge_version = minecraft_launcher_lib.forge.find_forge_version(version)
        print(forge_version)

        try:
            forgeLauch = forge_version.replace("-", "-forge-")
        except:
            print("forge version can be download or not exist")
            forgeLauch = None
        print(forgeLauch)

        # if you lauche minecraft vanilla
        if motor == "vanilla":
            minecraft_launcher_lib.install.install_minecraft_version(version, directory, callback=callback)

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
                                break
                    except:
                        None

                if checkVersionDoawnload() == None:
                    try:
                        print("doawnloading:" + forgeLauch)
                        minecraft_launcher_lib.forge.install_forge_version(forge_version, directory,
                                                                            callback=callback)
                        print(forgeLauch)

                    except:
                        None

        #self.ui.play.show()
        #self.ui.download.hide()

        login = getSelectVersion()
        print(login)

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

            passwordEnc = str(user + "67")
            password = password.replace("'", '')
            password = password[1:]
            print(password)
            username = username.replace("'", '')
            username = username[1:]
            print(username)
            pa = encrypte.password_decrypt(password, passwordEnc).decode()
            us = encrypte.password_decrypt(username, passwordEnc).decode()

            login_data = minecraft_launcher_lib.account.login_user(us, pa)
            print(login_data)
            options = {
                "username": login_data["selectedProfile"]["name"],
                "uuid": login_data["selectedProfile"]["id"],
                "token": login_data["accessToken"]
            }

            if motor == "vanilla":
                command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                options)
                execute_command(command)
            elif motor == "Forge":
                print("crack, lauching minecraft, version:" + forgeLauch)
                directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                    forgeLauch, directory, options)

                subprocess.call(minecraft_command)

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
                "token": uInfo["access_token"]
            }

            if motor == "vanilla":
                command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                options)
                execute_command(command)
            elif motor == "Forge":
                print("crack, lauching minecraft, version:" + forgeLauch)
                directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                    forgeLauch, directory, options)

                subprocess.call(minecraft_command)

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
                "token": ""
            }

            print(forge_version)
            print(motor)
            if motor == "vanilla":
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

                    subprocess.call(minecraft_command)
                except:
                    None

    else:
        version = n[0]
        
        motor = n[1]
        user = os.getlogin()
        def maximum(max_value, value):
            max_value[0] = value

        print('start minecraft')
        max_value = [0]

        def updateBar(value, maxValue):
            percent = 100 * int(value) / int(maxValue[0])
            #print(int(percent))
            #self.ui.download.setValue(percent)

        callback = {
            "setStatus": lambda text: print(text),
            "setProgress": lambda value: updateBar(value, max_value),
            "setMax": lambda value: maximum(max_value, value)
        }


        #self.ui.download.show()
        #self.ui.play.hide()
        print(motor)
        forge_version = minecraft_launcher_lib.forge.find_forge_version(version)
        print(forge_version)

        try:
            forgeLauch = forge_version.replace("-", "-forge-")
        except:
            print("forge version can be download or not exist")
            forgeLauch = None
        print(forgeLauch)

        #if you lauche minecraft vanilla
        if motor == "vanilla":
            minecraft_launcher_lib.install.install_minecraft_version(version, directory, callback=callback)

        #if you lauche ;inecrqft forge
        if motor == "Forge":
            if forge_version == "None":
                print("version non disponible de forge")

            else:
                def checkVersionDoawnload():
                    directory_mod = 'C:/Users/'+user+'\AppData\Roaming\.alpha67\minecraft/versions'
                    files = os.listdir(directory_mod)
                    for f in files:
                        print("file: "+f)
                        if forgeLauch == f:
                            print("version already download lauching minecraft")
                            return True
                            break

                if checkVersionDoawnload() == None:
                    try:
                        print("doawnloading:"+forgeLauch)
                        minecraft_launcher_lib.forge.install_forge_version(forge_version, directory,
                                                                            callback=callback)
                        print(forgeLauch)

                    except:
                        None

        #self.ui.play.show()
        #self.ui.download.hide()

        login = getSelectVersion()
        print(login)


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

            passwordEnc = str(user + "67")
            password = password.replace("'", '')
            password = password[1:]
            print(password)
            username = username.replace("'", '')
            username = username[1:]
            print(username)
            pa = encrypte.password_decrypt(password, passwordEnc).decode()
            us = encrypte.password_decrypt(username, passwordEnc).decode()

            login_data = minecraft_launcher_lib.account.login_user(us, pa)
            print(login_data)
            options = {
                "username": login_data["selectedProfile"]["name"],
                "uuid": login_data["selectedProfile"]["id"],
                "token": login_data["accessToken"]
            }


            if motor == "vanilla":
                command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                options)
                execute_command(command)
            elif motor == "Forge":
                print("crack, lauching minecraft, version:"+forgeLauch)
                directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                    forgeLauch, directory, options)

                subprocess.call(minecraft_command)


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
                "token": uInfo["access_token"]
            }

            if motor == "vanilla":
                command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                options)
                execute_command(command)
            elif motor == "Forge":
                print("crack, lauching minecraft, version:"+forgeLauch)
                directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                    forgeLauch, directory, options)

                subprocess.call(minecraft_command)

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
                "token": ""
            }

            print(forge_version)
            print(motor)
            if motor == "vanilla":
                command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                options)
                execute_command(command)
            elif motor == "Forge":
                try:
                    print("crack, lauching minecraft, version:"+forgeLauch)
                    directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                        forgeLauch, directory, options)
                    print(minecraft_command)

                    subprocess.call(minecraft_command)
                except:
                    None


def lauch():
    eel.returnInfo()(lambda n: start(n))
