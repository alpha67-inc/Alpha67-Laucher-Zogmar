from pydirectory.ldap.exceptions import *

class sAMAccountNameTooBig(customException):
	message = "sAMAccountName can't be bigger than 20 characters"
