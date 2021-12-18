import eel


# Set web files folder
eel.init('web')
  # Call a Javascript function

options = {
	'mode': 'custom',
	'args': ['node_modules/electron/dist/electron.exe', '.']
}

#print('Got this from Javascript:', n)

eel.start('hello.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron.exe', '.'])
