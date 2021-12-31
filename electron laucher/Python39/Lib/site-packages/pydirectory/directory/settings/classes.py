import socket
import getpass
import importlib
from pydirectory.directory import exceptions

class Option(object):
	def __init__(self,null=True,value=None,is_password=False,is_hostname=False,type=None,validator=None,description=None):
		self.null = null
		self.__type = type
		self.is_password=is_password
		self.is_hostname=is_hostname
		self.__validator = validator
		self.__doc__ = description
		if value == None:
			if not self.null:
				self._input_text()
			else:
				self.value = value
		else:
			self.value = value

	def _input_text(self):
		if self.is_password:
			self.value=getpass.getpass(self.__doc__+': ')
		else:
			self.value=input(self.__doc__+': ')

	def __iter__(self):
		return iter(self.value)

	def __str__(self):
		result = str(self.value)
		if self.is_password:
			raise exceptions.PasswordPrintNotAllowed
		return result

	def __eq__ (self,other):
		return self.value == other

	def __repr__(self):
		if type(self.value) == str:
			return self.value
		return repr(self.value)

	def __setattr__(self,name,value):
		if name == "value":
			if value != None:
				try:
					value = self.__type(value)
				except ValueError as e:
					raise exceptions.InvalidValueType(e)

				if self.__validator != None:
					if not self.__validator(value):
						raise exceptions.InvalidValue

			if self.is_hostname:
				try:
					self.ipv4 = socket.getaddrinfo(value,None,socket.AF_INET)[0][4][0]
				except socket.gaierror:
					self.ipv4 = False

				try:
					self.ipv6 = socket.getaddrinfo(value,None,socket.AF_INET6)[0][4][0]
				except socket.gaierror:
					self.ipv6 = False

				if (not self.ipv4) and (not self.ipv6):
					raise exceptions.DNSHostnameCanNotBeResolved

		super(Option,self).__setattr__(name,value)


class Settings(object):

	def __init__(self,type,**kwargs):
		self._exceptions = importlib.import_module("pydirectory.%(type)s.exceptions" % {'type':type})
		self.type = Option(null=False,type=str,description="Type engine",value=type)
		self._options(**kwargs)

	def __setattr__(self,name,value):
		if self.__dict__.get(name,False):
			self.__dict__[name].value = value
		else:
			if (type(value) != Option) and (name.find('_') != 0):
				raise self._exceptions.MustBeOptionType
			super(Settings,self).__setattr__(name,value)
