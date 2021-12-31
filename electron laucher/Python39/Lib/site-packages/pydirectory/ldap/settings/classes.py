from pydirectory.directory.settings.classes import Settings, Option

class settings(Settings):
	def _options(self,**kwargs):
		self.host = Option(null=False,type=str,is_hostname=True,description="Domain Controler Hostname or IP",value=kwargs.get('hostname',None))
		self.port = Option(type=int,description="Domain Controler Port connection",value=kwargs.get('port',None))
		self.username = Option(type=str,description="Username user connection",value=kwargs.get('username',None))
		passnull = True
		if self.username != None:
			passnull = False
		self.password = Option(null=passnull,type=str,is_password=True,description="Password user connection",value=kwargs.get('password',None))
		self.basedn= Option(type=str,description="LDAP base DN",value=kwargs.get('basedn',None))
		self.ssl= Option(type=bool,description="Enable SSL Connection (True/False)",value=kwargs.get('ssl',None))
		self.tls= Option(type=bool,description="Enable TLS Connection (True/False)",value=kwargs.get('tls',None))
