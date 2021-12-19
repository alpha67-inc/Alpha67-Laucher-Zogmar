import eel
import random


# Set web files folder
eel.init('web')


@eel.expose
def test():
	print("ok")
	return "ok"

options = {
	'mode': 'custom',
	'args': ['node_modules/electron/dist/electron.exe', '.']
}

#print('Got this from Javascript:', n)

eel.start('hello.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron.exe', '.'])
