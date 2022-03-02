from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QUrl, QLocale
import minecraft_launcher_lib
import json
import sys
import os

CLIENT_ID = "f2107422-b90b-46cf-9d04-3dd3da989b44"
SECRET = "I1G7Q~5IgcJGmIvT-jCzseZTZ2u6d8rJOf0cw"
REDIRECT_URL = "https://github.com/vultorio67/alpha67-downloader"


class LoginWindow(QWebEngineView):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Window Example")

        self.refresh_token_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "refresh_token.json")

        # Login with refresh token, if it exists
        user = os.getlogin()
        """ if os.path.isfile("C:/Users/"+user+"\AppData\Roaming\.alpha67/alpha/microcred.json"):
            with open("C:/Users/"+user+"\AppData\Roaming\.alpha67/alpha/microcred.json", "r", encoding="utf-8") as f:
                refresh_token = json.load(f)
                # Do the login with refresh token
                try:
                    account_informaton = minecraft_launcher_lib.microsoft_account.complete_refresh(CLIENT_ID, SECRET,
                                                                                                   REDIRECT_URL,
                                                                                                   refresh_token)
                    print(account_informaton)
                    with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/ACI.json", "w",
                              encoding="utf-8") as f:
                        json.dump(account_informaton, f)
                    self.show_account_information(account_informaton)

                    return
                # Show the window if the refresh token is invalid
                except minecraft_launcher_lib.exceptions.InvalidRefreshToken:
                    pass"""

        print("ok2")
        print(minecraft_launcher_lib.microsoft_account.get_login_url(CLIENT_ID, REDIRECT_URL))
        self.load(QUrl(minecraft_launcher_lib.microsoft_account.get_login_url(CLIENT_ID, REDIRECT_URL)))
        print("ok3")
        # Connects a function that is called when the url changed
        self.urlChanged.connect(self.new_url)

        print("ok4")
        self.show()

    def new_url(self, url: QUrl):

        print("ok5")

        print(url)
        # Check if the url contains the code
        if minecraft_launcher_lib.microsoft_account.url_contains_auth_code(url.toString()):

            print("ok")
            # Get the code from the url
            auth_code = minecraft_launcher_lib.microsoft_account.get_auth_code_from_url(url.toString())

            print(auth_code)
            # Do the login


            account_informaton = minecraft_launcher_lib.microsoft_account.complete_login(CLIENT_ID, SECRET, REDIRECT_URL, auth_code)

            print(account_informaton)

            # Show the login information
            self.show_account_information(account_informaton)

    def show_account_information(self, information_dict):


        print(f'Username: {information_dict["name"]}<br>')
        print(f'Username: {information_dict["id"]}<br>')
        print(f'Username: {information_dict["access_token"]}<br>')

        username = information_dict["name"]
        id = information_dict["id"]
        access_token = information_dict["access_token"]

        # Save the refresh token in a file
        user = os.getlogin()
        with open("C:/Users/"+user+"\AppData\Roaming\.alpha67/alpha/microcred.json", "w", encoding="utf-8") as f:
            json.dump(information_dict["refresh_token"], f, ensure_ascii=False, indent=4)

        with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/ACI.json", "w",
                  encoding="utf-8") as f:
            json.dump(information_dict, f)

        with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
            data = json.load(jsonFile)
            print(data)

        data["microsoft"][0]["connect"] = "True"
        data["microsoft"][0]["select"] = "True"
        data["mojang"][0]["select"] = "False"
        data["crack"][0]["select"] = "False"
        print(data)

        with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "w") as jsonFile:
            json.dump(data, jsonFile)

        information_string = f'Username: {information_dict["name"]}<br>'
        information_string += f'UUID: {information_dict["id"]}<br>'
        information_string += f'Token: {information_dict["access_token"]}<br>'

        message_box = QMessageBox()
        message_box.setWindowTitle("Account information")
        message_box.setText(information_string)
        message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.close()
        message_box.exec()

        # Exit the program
        sys.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # This line sets the language of the webpage to the system language
    QWebEngineProfile.defaultProfile().setHttpAcceptLanguage(QLocale.system().name().split("_")[0])
    w = LoginWindow()
    sys.exit(app.exec())
