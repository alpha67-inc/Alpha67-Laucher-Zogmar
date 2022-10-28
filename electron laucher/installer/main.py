import time
import json
from ttkbootstrap import Style
from tkinter.ttk import Progressbar
from tkinter.messagebox import askquestion, showinfo
from tkinter import Label, Canvas, PhotoImage
from tkinter import messagebox, Tk

import sys
import os
import time

from tkinter import *
import threading

import urllib.request
from zipfile import ZipFile
import shutil

import crashreport

import subprocess

def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')

    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)


class MainWindow():

    try:
        #partie graphique
        def __init__(self):
                style = Style()

                self.ui = "salut"

                self.hello()

                self.root = style.master
                self.root.configure(bg="#3a3a3a")
                self.root.title("Capitalium Factory Updater")
                self.root.geometry("761x403+140+50")
                self.root.iconbitmap("icon.ico")

                Tk_Width = 761
                Tk_Height = 403

                x_Left = int(self.root.winfo_screenwidth() / 2 - Tk_Width / 2)
                y_Top = int(self.root.winfo_screenheight() / 2 - Tk_Height / 2)

                self.root.geometry(f"+{x_Left}+{y_Top}")

                self.root.resizable(False, False)

                self.canvas = Canvas(
                self.root,
                bg="#3a3a3a",
                height=768,
                width=1024,
                bd=0,
                highlightthickness=0,
                relief="ridge")
                self.canvas.place(x=-1, y=0)


                background_img = PhotoImage(file="img/mc1.png")
                background = self.canvas.create_image(
                380.5, 201.5,
                image=background_img)

                self.info = self.canvas.create_text(
                395, 350,
                text="Getting everything ready.....",
                fill="#c4c4c4",
                font=("Segou Print", int(16.0)))


                # l1 = Label(root)

                #self.root = tk.Tk()

                #self.label = tk.Label(self.root, text="Text")

                #self.label.pack()

                #print(self.var)

                pb1 = Progressbar(self.root, value=0, style='info.Horizontal.TProgressbar', length=400, mode="indeterminate")
                pb1.place(x=200, y=400)

                window_running = True
                pb1.start()


                # root.after(20000, lambda: pb1.stop())


                """if t1.is_alive() or t2.is_alive():
                    pb1.stop()"""

                try:
                    print("ok")
                    #print(self.var)
                    self.root.mainloop()

                except KeyboardInterrupt:
                    print("Program Exited")

        def hello(self):
            th1 = threading.Thread(target=self.smart)
            th1.start()
            #th1.stop
            #print(self.var)
    except:
        import traceback
        traceback.print_exc()
















#partie installation
    def smart(self):

        try:

            with open("C:/Users/"+user+"/AppData/Local/laucher67/app/infLau.json") as json_file:

                data = json.load(json_file)
                print(data)

                executable = data["executable-name"]

            try:
                os.system("taskkill /im "+ executable)
                os.system("taskkill /im Electron.exe")
            except:
                print("can't kill"+executable+"or the process not exist")

        except:
            print("can't find file infLau.json")

        try:

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

            def updateAll():

                user = os.getlogin()

                try:

                    with open("C:/Users/"+user+"/AppData/Local/laucher67/app/infLau.json") as json_file:

                        data = json.load(json_file)
                        print(data)

                        executable = data["executable-name"]

                    try:
                        os.system("taskkill /im "+ executable)
                        os.system("taskkill /im Electron.exe")
                    except:
                        print("can't kill"+executable+"or the process not exist")

                except:
                    print("can't find file infLau.json")




                

                response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/alpha67-laucher/releases")
                data = json.loads(response.read())
                print(data)
                data = data[0]
                data = data["assets"]
                data = data[0]
                url = data["browser_download_url"]

                response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/alpha67-laucher/releases")
                data = json.loads(response.read())
                data = data[0]
                version = data["tag_name"]



                time.sleep(0.4)
                print("supression de fichier.")

                print(os.listdir("C:/Users/"+user+"/AppData\Local\laucher67/"))

                shutil.rmtree("C:/Users/"+user+"/AppData\Local\laucher67/")

                try:
                    None
                except:
                    try:

                        os.remove("C:/Users/"+user+"/AppData\Local\laucher67/")
                    except:
                        None
                    print("can't remove file")


                user = os.getlogin()
                print(url)
                print("starting download")

                try: 
                    os.mkdir("C:/Users/"+user+"/AppData\Local\laucher67/") 
                except OSError as error: 
                    print(error)  

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
                    
                    self.canvas.itemconfig(self.info, text=tex)

                folder = "C:/Users/"+user+"/AppData\Local\laucher67/app.zip"

                urllib.request.urlretrieve(url, folder, cbk)
                
                with ZipFile("C:/Users/"+user+"/AppData\Local\laucher67/app.zip", 'r') as zip:
                    zip.printdir()
                    zip.extractall("C:/Users/"+user+"/AppData\Local\laucher67/")

                f = open("C:/Users/"+user+"/AppData\Local\laucher67/version.txt", "w")
                f.write(str(version))
                f.close()



            def checkUpdate():
                response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/alpha67-laucher/releases")
                data = json.loads(response.read())
                data = data[0]
                version = data["tag_name"]
                print(version)

                try:

                    f = open("C:/Users/"+user+"/AppData\Local\laucher67/version.txt", "r")
                    txtVersion = f.read()

                    if txtVersion != version:
                        return True
                    else:
                        return False
                    # Do something with the file
                except IOError:
                    print("File not accessible, starting his creation")
                    return True

            MYDIR = "C:/Users/"+user+"/AppData\Local\laucher67"
            CHECK_FOLDER = os.path.isdir(MYDIR)
            # If folder doesn't exist, then create it.
            if not CHECK_FOLDER:

                time.sleep(0.5)
                self.canvas.itemconfig(self.info, text="téléchargement du laucher...")

                os.makedirs(MYDIR)
                print("created folder : ", MYDIR)
                createDirectory("laucher67", "C:/Users/"+user+"/AppData\Local/")
                updateAll()
                time.sleep(1)
                update = True
                needGetJsonAdress = False

            import pathlib
            file = pathlib.Path("C:/Users/"+user+"/AppData/Local/laucher67/app/app.exe")
            if file.exists ():
                print ("File exist")
            else:
                alert("INFO", "the executable app.exe witch lauch the laucher can not be found !! if the message reappears several times it is probably that your anttivirus detects this laucher as a virus. To resolve the problem disabled your antivirus or contact a developer of the laucher.", kind="warning")
                updateAll()


            MYDIR = "C:/Users/"+user+"\AppData\Roaming\.alpha67"
            CHECK_FOLDER = os.path.isdir(MYDIR)
            # If folder doesn't exist, then create it.
            if not CHECK_FOLDER:
                os.makedirs(MYDIR)
                print("created folder : ", MYDIR)
                createDirectory(".alpha67", "C:/Users/"+user+"\AppData\Roaming")
                update = True
                needGetJsonAdress = False

            MYDIR = "C:/Users/" + user + "\AppData\Roaming\.alpha67/minecraft"
            CHECK_FOLDER = os.path.isdir(MYDIR)
            # If folder doesn't exist, then create it.
            if not CHECK_FOLDER:
                os.makedirs(MYDIR)
                print("created folder : ", MYDIR)
                createDirectory("minecraft", "C:/Users/" + user + "\AppData\Roaming\.alpha67/")
                update = True
                needGetJsonAdress = False

            MYDIR = "C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha"
            CHECK_FOLDER = os.path.isdir(MYDIR)
            # If folder doesn't exist, then create it.
            if not CHECK_FOLDER:
                os.makedirs(MYDIR)
                print("created folder : ", MYDIR)
                createDirectory("alpha", "C:/Users/" + user + "\AppData\Roaming\.alpha67/")
                update = True
                needGetJsonAdress = False

            """        if os.path.isfile("C:/Users/"+user+"\AppData\Roaming\.alpha67/install-data.json") == False:
                print("create data folder")
                print("Installing java 16.....")
                time.sleep(1)
                self.canvas.itemconfig(self.info, text="telechargement de java, veuillez patientez...")
                wget.download("https://download.bell-sw.com/java/16.0.2+7/bellsoft-jdk16.0.2+7-windows-amd64.msi",bar=wget.bar_adaptive)
                filename = wget.detect_filename("https://download.bell-sw.com/java/16.0.2+7/bellsoft-jdk16.0.2+7-windows-amd64.msi")
                self.canvas.itemconfig(self.info, text="installation de java, suivez les instructions...")
                os.system(f"msiexec /i {filename}")
                time.sleep(1)
                print("java ok")
                with open("C:/Users/"+user+"\AppData\Roaming\.alpha67/install-data.json", 'w') as outfile:
                    json.dump(str({"java": "ok"}), outfile)"""

            time.sleep(1)

            self.canvas.itemconfig(self.info, text="Recherche de mise à jour, veuillez patientez...")
            if checkUpdate() == True:
                self.canvas.itemconfig(self.info, text="mise à jour du laucher...")
                updateAll()
            time.sleep(1)

            self.canvas.itemconfig(self.info, text="Démarrage du laucher...")

            #        self.canvas.itemconfig(self.info, text="Demarrage du laucher...")

            time.sleep(1)

            def subprocess_cmd(command):
                process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
                proc_stdout = process.communicate()[0].strip()
                print (proc_stdout)

            #subprocess_cmd("cd  C:/Users/"+user+"\AppData\Local\laucher67/app/; C:/Users/"+user+"\AppData\Local\laucher67/app/app.exe")
            print(self.info)

            subprocess.call(r"start.bat")

            time.sleep(1)

            root.destroy()

            os._exit(0)

            sys.exit()

        except Exception:
            root.destroy()
            Tk().withdraw()
            alert('Error', 'The laucher have crash please see crash report to have more info aboute what is getting wrong.', kind="error")
            cause = None
            try:
                5 + 's'
            except TypeError as e:
                cause = e
            raise ValueError('exception raised') from cause














if __name__ == "__main__":

    crashreport.inject_excepthook(lambda etype, value, tb, dest: print('Dumped crash report to', dest))

    try:
        root = Tk()

        my_gui = MainWindow()
        root.mainloop()
        time.sleep(2)
    except Exception:
        Tk().withdraw()
        alert('Error', 'The laucher have crash please see crash report to have more info aboute what is getting wrong.', kind="error")
        cause = None
        try:
            5 + 's'
        except TypeError as e:
            cause = e
        raise ValueError('exception raised') from cause
