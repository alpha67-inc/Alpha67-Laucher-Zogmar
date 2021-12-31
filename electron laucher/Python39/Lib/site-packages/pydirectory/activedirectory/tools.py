from pydirectory.ldap.tools import *
#from datetime import timedelta, tzinf

class setQuery(setQuery):
	specialFields = {
		'is_disable' : {
	 		True: '(userAccountControl:1.2.840.113556.1.4.803:=2)',
			False: '(!(userAccountControl:1.2.840.113556.1.4.803:=2))',
		},
		'is_enable' : {
	 		True: '(!(userAccountControl:1.2.840.113556.1.4.803:=2))',
			False: '(userAccountControl:1.2.840.113556.1.4.803:=2)',
		},
		'is_member': '(memberof:1.2.840.113556.1.4.1941:={DN})',
		'in_group': '(member:1.2.840.113556.1.4.1941:={DN})'
	}

# from python standard library docs
class OffsetTzInfo(object):
	from datetime import tzinfo
	class OffsetTzInfo(tzinfo):
		"""Fixed offset in minutes east from UTC"""

		def __init__(self, offset, name):
			import datetime
			self.datetime = datetime
			self.offset = offset
			self.name = name
			self._offset = self.datetime.timedelta(minutes=offset)
			self.name = name

		def __str__(self):
			return self.name

		def __repr__(self):

			return 'OffsetTzInfo(offset={0.offset!r}, name={0.name!r})'.format(self)

		def utcoffset(self, dt):
			return self._offset

		def tzname(self, dt):
			return self.name

		def dst(self, dt):
			return self.datetime.timedelta(0)

	def __init__(self,*args,**kwargs):
		pass
