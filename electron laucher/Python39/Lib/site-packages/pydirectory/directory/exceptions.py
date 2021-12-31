class customException(Exception):
	def __init__(self,message=False):
		if message:
			self.message=message

	def __str__(self):
		return repr(self.message)


class NotValidController(customException):
	message = "Not Valid Controller"

class InvalidServer(customException):
	message = "Invalid Host or Server Name"

class UnknownError(customException):
	message = "Unknown Error"

class InvalidCredentials(customException):
	message = "Invalid username y/or password"

class AttributeNotValid(customException):
	message = "The attribute is not valid"

class SettingsOptionNotExist(customException):
	message = "The Settings Option to set not exist"

class InvalidValueType(customException):
	message = "Invalid value type"

class InvalidValue(customException):
	message = "Invalid value"

class MustBeOptionType(customException):
	message = "Value must be Option type"

class PasswordPrintNotAllowed(customException):
	message = "Password Print is not Allowed"

class DNSHostnameCanNotBeResolved(customException):
	message = "DNS Hostname Can not be resolved"

class MultipleResults(customException):
	message = "The response has returned multiple results"

class ObjectIsModified(customException):
	message = "The object is modified. You can not delete or append attributes values"

class ObjectNotExist(customException):
	message = "The object not exist"

class AttributeisReadOnly(customException):
	message = "The attribute is read only"

class CheckValueAttributes(customException):
	message = "Some attribute value is not correct"

class IsReadOnly(customException):
	message = "The action is not permitted. It is read only"

class isNaN(customException):
	message = "attribute is not a number"
