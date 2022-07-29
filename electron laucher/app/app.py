import eel
import random
from pythonSide import *
import time
import traceback
import crashreport
crashreport.inject_excepthook(lambda etype, value, tb, dest: print('Dumped crash report to', dest))

def main_div_by_0():
	import subprocess 
	eel.init('web')
	print("okokokokokokok")
	start()




	@eel.expose
	def test():
		print("ok")
		return "ok"

	@eel.expose
	def sendVersions():
		version = ["alpha67"]

		for i in getVersions():
			# Only add release versions
			if i["type"] == "release":
				if not "fo" in i["id"]:
					version.append(i["id"])

		return version

	options = {
		'mode': 'custom',
		'args': ['node_modules/electron/dist/electron.exe', '.']
	}

	def print_num(n):
		print('Got this from Javascript:', n)

	
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

	java = data["java"]


	if java == "auto":
		java = "C:/Users/"+user+"/AppData/Roaming/.alpha67/jdk-18.0.2/bin/javaw.exe"
		with open('C:/Users/'+user+'/AppData/Roaming\.alpha67/alpha/settings.json', 'r+') as f:
			data = json.load(f)
			data['java'] = java# <--- add `id` value.
			#f.seek(0)        # <--- should reset file position to the beginning.

		with open('C:/Users/'+user+'/AppData/Roaming\.alpha67/alpha/settings.json', 'w') as outfile:
			print("save : ", data)
			json.dump(data, outfile)  


	eel.start('hello.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron.exe', '.'])

	#eel.start('hello.html')

	time.sleep(5)


def main_double():
    try:
        main_div_by_0()
    except Exception:
        cause = None
        try:
            5 + 's'
        except TypeError as e:
            cause = e
        raise ValueError('exception raised') from cause


def main_recursion():
    x = 5
    main_recursion()


if __name__ == '__main__':
	main_double()
	




