import importlib

class Engine(object):
	def __init__(self,settings,autologin=True):
		self._exceptions = importlib.import_module("pydirectory.%(type)s.exceptions" % {'type':settings.type})
		self._settings = settings
		if autologin:
			self.login()

	def authenticate(self,username,password):
		return False

	def login(self):
		return False
