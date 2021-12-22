import eel
import os
import minecraft_launcher_lib

import sys
sys.path.append("..")
import json

from cryptography.fernet import Fernet


def upass():
    user = os.getlogin()
    #userName = uia.lineEdit.text()
    #password = uia.lineEdit_2.text()


    def exportCred(n):
        userName = str(n[0])
        password = str(n[1])
        print(userName)



        login_data = minecraft_launcher_lib.account.login_user(userName, password)
        print(login_data)

        try:
            print(login_data['error'])
            eel.invalid()

        except:
            print("True login")
            loginUsername= login_data["selectedProfile"]["name"]
            uuid= login_data["selectedProfile"]["id"]
            token= login_data["accessToken"]

            userName = userName.replace("'", "")
            password = password.replace("'", "")

            userName = userName.replace("b", "")
            password = password.replace("b", "")
            #uia.info.setText("Identification reussi =)")

            key = Fernet.generate_key()
            fernet = Fernet(key)
            encUserName = fernet.encrypt(userName.encode())
            encPassword = fernet.encrypt(password.encode())

            def crack():
                try:
                    with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'r') as file:
                        uInfo = json.load(file)
                        # uInfo = literal_eval(uInfo)

                        uInfo = uInfo['crack']
                        uInfo = uInfo[0]
                        print(uInfo)
                        uInfo = uInfo['username']
                        print(uInfo)
                        return uInfo
                except:
                    return None

            x = {

                "mojang": [
                    {"username": str(encUserName), "password": str(encPassword), "loginUsername": loginUsername, "uuid": uuid,"token": token, "key": str(key)}
                ],
                "crack": [
                    {"username": crack()}
                ]
            }

            with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'w') as outfile:
                json.dump(x, outfile)

            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                data = json.load(jsonFile)
                print(data)

            data["mojang"][0]["connect"] = "True"
            data["mojang"][0]["select"] = "True"
            data["microsoft"][0]["select"] = "False"
            data["crack"][0]["select"] = "False"
            print(data)

            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "w") as jsonFile:
                json.dump(data, jsonFile)

            eel.finish()

    eel.getCred()(lambda n: exportCred(n))



