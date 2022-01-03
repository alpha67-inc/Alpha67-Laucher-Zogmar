import json
import os
import eel

user = os.getlogin()

def crack():
    def exportCred(n):
        try:
            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/cred.json", "r") as jsonFile:
                data = json.load(jsonFile)

            data["crack"][0]['username'] = str(n)
            print(data["crack"][0]['username'])

            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/cred.json", "w") as jsonFile:
                json.dump(data, jsonFile)

            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                data = json.load(jsonFile)
                print(data)

            data["crack"][0]["connect"] = "True"
            data["crack"][0]["select"] = "True"
            data["microsoft"][0]["select"] = "False"
            data["mojang"][0]["select"] = "False"
            print(data)

            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "w") as jsonFile:
                json.dump(data, jsonFile)

            eel.finish()

        except:
            print("error")
            x = {
                "crack": [
                    {"username": str(n)}
                ]
            }

            with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'w') as outfile:
                json.dump(x, outfile)

            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                data = json.load(jsonFile)
                print(data)

            data["crack"][0]["connect"] = "True"
            data["crack"][0]["select"] = "True"
            data["microsoft"][0]["select"] = "False"
            data["mojang"][0]["select"] = "False"
            print(data)

            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "w") as jsonFile:
                json.dump(data, jsonFile)

            eel.finish()

    eel.getCredCrack()(lambda n: exportCred(n))