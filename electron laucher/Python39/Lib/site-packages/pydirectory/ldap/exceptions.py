from pydirectory.directory.exceptions import *
from ldap3.core.exceptions import LDAPSocketOpenError,LDAPInvalidFilterError,LDAPChangeError,LDAPInvalidCredentialsResult,LDAPSocketSendError,LDAPOperationsErrorResult,LDAPEntryAlreadyExistsResult,LDAPUnwillingToPerformResult, LDAPNoSuchObjectResult
from pyasn1.error import PyAsn1Error

class LDAPError(customException):
	pass


class LDAPReferrals(LDAPError):
	pass

class DNisNone(customException):
	message = "DN is None"
