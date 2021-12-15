import eel

# Set web files folder
eel.init('web')
  # Call a Javascript function

#            <h1>Alpha67 Laucher</h1>
 #           <button class="glow-on-hover" type="button">HOVER ME, THEN CLICK ME!</button>
options = {
	'mode': 'custom',
	'args': ['node_modules/electron/dist/electron.exe', '.']
}

#eel.start('hello.html', mode='edge')
eel.start('hello.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron.exe', '.'])
