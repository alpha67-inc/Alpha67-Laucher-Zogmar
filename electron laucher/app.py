import eel
import random
from pythonSide import *


# Set web files folder
eel.init('web')

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

#print('Got this from Javascript:', n)

eel.start('hello.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron.exe', '.'])
#eel.start('hello.html')
