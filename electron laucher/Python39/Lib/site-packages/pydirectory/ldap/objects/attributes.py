from pydirectory.directory.objects import attributes
from ldap3 import MODIFY_REPLACE


class attribute(attributes.attribute):
	_is_rdn = False
	_operator = MODIFY_REPLACE

class cn(attribute):
	_is_rdn = True

class dn(attribute):
	_is_readonly = True
	_is_rdn = True

class container(attribute):
	_is_rdn = True
