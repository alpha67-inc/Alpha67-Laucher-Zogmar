from pydirectory.ldap.objects.attributes import *

class sAMAccountName(attribute):
	def _toraw(self,value):
		checklen = False
		if str == bytes: #is python2
			if isinstance(value,basestring):
				checklen = True
		else:
			if isinstance(value,str):
				checklen = True
		if checklen:
			if not (len(value) <= 20):
				raise self._exceptions.sAMAccountNameTooBig
		super(sAMAccountName,self)._toraw(value)

class PrimaryGroupID(attribute):
	def _tovalue(self):
		sid = '%(base)s-%(id)s' % {
			'base':self._objects.base.objectsid.value,
			'id':int(self.raw[0])
		}
		return self._objects.get(self._objects.setQuery(objectsid=sid))

class member(attribute):
	_is_readonly = True

	@property
	def raw(self):
		if self._raw[0] == None:
			member = []
			init = 0
			for end in range(1500,10000,1500):
				try:
					fieldname = 'member;range=%(init)s-%(end)s' % {"init":init,"end":end-1}
					fieldwildcard = 'member;range=%(init)s-*' % {"init":init}
					result = self._objects.search(dn=self._id,attributes=[fieldname])[0]
					if fieldname in result.attributes.keys():
						member.extend(result.attributes[fieldname])
					if fieldwildcard in result.attributes.keys():
						member.extend(result.attributes[fieldwildcard])
					init=end
				except self._exceptions.LDAPOperationsErrorResult:
					self._raw = member

		return self._raw

class memberOf(attribute):
	_is_readonly = True

class userAccountControl(attribute):
	types = {
		"SCRIPT" : 1,
		"ACCOUNTDISABLE" : 2,
		"HOMEDIR_REQUIRED" : 8,
		"LOCKOUT" : 16,
		"PASSWD_NOTREQD" : 32,
		"ENCRYPTED_TEXT_PWD_ALLOWED" : 128,
		"TEMP_DUPLICATE_ACCOUNT" : 256,
		"NORMAL_ACCOUNT" : 512,
		"INTERDOMAIN_TRUST_ACCOUNT" : 2048,
		"WORKSTATION_TRUST_ACCOUNT" : 4096,
		"SERVER_TRUST_ACCOUNT" : 8192,
		"DONT_EXPIRE_PASSWORD" : 65536,
		"MNS_LOGON_ACCOUNT" : 131072,
		"SMARTCARD_REQUIRED" : 262144,
		"TRUSTED_FOR_DELEGATION" : 524288,
		"NOT_DELEGATED" : 1048576,
		"USE_DES_KEY_ONLY" : 2097152,
		"DONT_REQ_PREAUTH" : 4194304,
		"PASSWORD_EXPIRED" : 8388608,
		"TRUSTED_TO_AUTH_FOR_DELEGATION" : 16777216
	}

	def accountControl(self,options):
		val = 0
		for type in options:
			val = val + self.types.get(type,0)
		return val

	def _toraw(self,value):
		if type(value) == list:
			acControl = self.accountControl(value)
			if acControl > 0:
				self._raw = [str(acControl)]
			else:
				self._raw = value
		else:
			self._raw = [value]

	def _tohuman(self):
		try:
			binary = bin(int(self.value))[2:][::-1]
		except:
			return self.value
		values = []
		for bit in range(0,len(binary)):
			if binary[bit] == '1':
				decimal = int(binary[bit]+'0'*bit,2)
				try:
					position = list(self.types.values()).index(decimal)
					value = list(self.types.keys())[position]
					values.append(value)
				except:
					values.append("UNKNOWN")
		return values


class unicodePwd(attribute):
	def _toraw(self,value):
		try:
			password = ('"%s"' % value).encode('utf-16-le')
		except UnicodeDecodeError:
			password = ('"%s"' % value.decode('utf-8')).encode('utf-16-le')
		self._raw = [password]

	def _tohuman(self):
		raise self._exceptions.PasswordPrintNotAllowed


class ObjectSid(attribute):
	_is_readonly = True

	def _littleEndian(self,hex):
		result = '';
		xinit = len(hex) - 2
		for x in range(xinit,0-1,-2):
			result += hex[x:x+2]
		return result

	def _getTextSID(self,binsid):
		import binascii
		hex_sid = binascii.hexlify(binsid).decode('utf-8')
		subcount = int(hex_sid[2:2+2],16)
		rev = int(hex_sid[0:0+2],16)
		auth = int(hex_sid[4:4+12],16)
		result = str(rev)+'-'+str(auth)
		subauth = {}
		for x in range(0,subcount):
			le = hex_sid[16+(x*8):(16+(x*8))+8]
			subauth[x] = int(self._littleEndian(le),16)
			try:
				result += '-'+str(subauth[x])
			except TypeError:
				result += '-'+bytes(subauth[x])
		return 'S-'+result

	def _tovalue(self):
		return self._getTextSID(self.raw[0]).decode('utf-8')


class sIDHistory(ObjectSid):
	pass


class ObjectGUID(attribute):
	_is_readonly = True
	def _tovalue(self):
		import uuid
		return str(uuid.UUID(bytes=self.raw[0])).decode('utf-8')


class formattime(attribute):
	_is_readonly = True
	def _tovalue(self):
		#Hack from ldap3.protocol.formatters.formatters.format_time https://github.com/cannatag/ldap3
		from pydirectory.activedirectory.tools import OffsetTzInfo
		from datetime import datetime
		raw_value = self.raw[0]
		if len(raw_value) < 10 or not all((c in b'0123456789+-,.Z' for c in raw_value)) or (b'Z' in raw_value and not raw_value.endswith(b'Z')):  # first ten characters are mandatory and must be numeric or timezone or fraction
			return raw_value

		year = int(raw_value[0: 4])
		month = int(raw_value[4: 6])
		day = int(raw_value[6: 8])
		hour = int(raw_value[8: 10])
		minute = 0
		second = 0
		microsecond = 0

		remain = raw_value[10:]
		if remain and remain.endswith(b'Z'):  # uppercase 'Z'
			sep = b'Z'
		elif b'+' in remain:  # timezone can be specified with +hh[mm] or -hh[mm]
			sep = b'+'
		elif b'-' in remain:
			sep = b'-'
		else:  # timezone not specified
			return raw_value

		time, _, offset = remain.partition(sep)

		if time and (b'.' in time or b',' in time):
			# fraction time
			if time[0] in b',.':
				minute = 6 * int(time[1] if str == bytes else chr(time[1]))
			elif time[2] in b',.':
				minute = int(raw_value[10: 12])
				second = 6 * int(time[3] if str == bytes else chr(time[3]))
			elif time[4] in b',.':
				minute = int(raw_value[10: 12])
				second = int(raw_value[12: 14])
				microsecond = 100000 * int(time[5] if str == bytes else chr(time[5]))
			elif len(time) == 2:  # mmZ format
				minute = int(raw_value[10: 12])
			elif len(remain) == 0:  # Z format
				pass
			elif len(time) == 4:  # mmssZ
				minute = int(raw_value[10: 12])
				second = int(raw_value[12: 14])
			else:
				return raw_value

			if sep == b'Z':  # UTC
				timezone = OffsetTzInfo.OffsetTzInfo(0, 'UTC')
			else:  # build timezone
				try:
					if len(offset) == 2:
						timezone_hour = int(offset[:2])
						timezone_minute = 0
					elif len(offset) == 4:
						timezone_hour = int(offset[:2])
						timezone_minute = int(offset[2:4])
					else:  # malformed timezone
						raise ValueError
				except ValueError:
					return raw_value
				if str != bytes:  # python3
					timezone = OffsetTzInfo.OffsetTzInfo((timezone_hour * 60 + timezone_minute) * (1 if sep == b'+' else -1), 'UTC' + str(sep + offset, encoding='utf-8'))
				else:
					timezone = OffsetTzInfo.OffsetTzInfo((timezone_hour * 60 + timezone_minute) * (1 if sep == b'+' else -1), unicode('UTC' + sep + offset, encoding='utf-8'))

			try:
				return datetime(year=year,
								month=month,
								day=day,
								hour=hour,
								minute=minute,
								second=second,
								microsecond=microsecond,
								tzinfo=timezone)
			except (TypeError, ValueError):
				return raw_value


class WhenCreated(formattime):
	pass

class WhenChanged(formattime):
	pass

class dSCorePropagationData(formattime):
	pass

class adTimeStamp(attribute):
	_is_readonly = True
	def _tovalue(self):
		#Hack from ldap3.protocol.formatters.formatters.format_ad_timestamp https://github.com/cannatag/ldap3
		from pydirectory.activedirectory.tools import OffsetTzInfo
		from datetime import datetime
		try:
			timestamp = int(self.raw[0])
			return datetime.fromtimestamp(timestamp / 10000000.0 - 11644473600, tz=OffsetTzInfo.OffsetTzInfo(0, 'UTC'))
		except Exception:
			if self.raw[0] == b'9223372036854775807':
				return datetime.max
			return self.raw[0]

class creationTime(adTimeStamp):
	pass

class pwdLastSet(adTimeStamp):
	pass

class badPasswordTime(adTimeStamp):
	pass

class lastLogon(adTimeStamp):
	pass

class lastLogonTimeStamp(adTimeStamp):
	pass

class accountExpires(adTimeStamp):
	pass

class maxPwdAge(adTimeStamp):
	pass

class minPwdAge(adTimeStamp):
	pass

class countryCode(attribute):
	def _toraw(self,value):
		if type(value) == list:
			aux = value[0]
		else:
			aux = value
		if not aux.isdigit():
			raise self._exceptions.isNaN
		self._raw = [aux]
