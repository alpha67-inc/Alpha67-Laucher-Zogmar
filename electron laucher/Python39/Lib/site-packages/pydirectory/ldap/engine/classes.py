from ldap3 import Server, Connection, ALL, SUBTREE, BASE
from pydirectory.directory.engine.classes import Engine

class engine (Engine):

	def _authenticate(self,username,password,login=False):
		server_options = {
		 'host': repr(self._settings.host),
		 'use_ssl': self._settings.ssl.value,
		 'get_info': ALL
		}
		if self._settings.port.value != None:
			server_options['port'] = self._settings.port.value

		server = Server(**server_options)
		conn = Connection(server, user=username,password=password,auto_referrals=False,raise_exceptions=True)
		result = False
		try:
			result = conn.bind()
		except self._exceptions.LDAPSocketOpenError:
			raise self._exceptions.InvalidServer
		except self._exceptions.LDAPInvalidCredentialsResult:
			raise self._exceptions.InvalidCredentials


		if self._settings.port.value == None:
			self._settings.port = conn.server.port

		if login:
			if result == False:
				raise self._exceptions.InvalidCredentials
			if self._settings.basedn == None:
				self._settings.basedn = conn.server.info.raw['defaultNamingContext'][0].decode('utf-8') #fix to convert byte to string
			return conn
		return result


	def login(self):
		self._worker = self._authenticate(repr(self._settings.username),repr(self._settings.password),login=True)

	def authenticate(self,username,password):
		return self._authenticate(username,password)
