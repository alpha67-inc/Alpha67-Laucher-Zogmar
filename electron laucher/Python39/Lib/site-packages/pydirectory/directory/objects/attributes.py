# -*- coding: utf-8 -*-
class attribute(object):
	_is_readonly = False
	def __init__(self,value,objects,objid=None,modify=True):
		self._id = objid
		self._objects = objects
		self._exceptions = self._objects._exceptions
		self._is_modified = False
		self._is_append = False
		self._is_delete = False
		self._delattr = []
		self._addattr = []
		self._toraw(value)

		if modify:
			self._is_modified = True
		else:
			self._is_modified = False

	def _toraw(self,value):
		if not (type(value) == list):
			self._raw = [value]
		elif value == None:
			self._raw = [None]
		else:
			self._raw = value

	def __str__(self):
		if (type(self._tohuman()) == str):
			return self._tohuman()
		else:
			human = self._tohuman()
			if str == bytes: #Is python 2
				if type(human) == unicode:
					return human.encode('utf-8')
			return str(human)

	def __unicode__(self): #fix python 2.7 compatibility
		if (type(self._tohuman()) == str):
			return self._tohuman().decode('utf-8')
		else:
			return unicode(self._tohuman())

	def __repr__(self):
		if type(self._tohuman()) == str:
			return self._tohuman()
		else:
			return repr(self._tohuman())

	def __setitem__(self,key,value):
		if self._is_readonly:
			raise self._exceptions.IsReadOnly
		self._raw[key] = value

	def __getitem__(self,key):
		return self.raw[key]

	def __len__(self):
		return len(self.raw)

	def __delitem__(self,key):
		if self._is_readonly:
			raise self._exceptions.IsReadOnly
		if self._is_modified:
			raise self._exceptions.ObjectIsModified
		value = self._raw[key]
		changed = False
		if value in self._addattr:
			key = self._addattr.index(value)
			del self._addattr[key]
			changed = True
		if not value in self._delattr:
			self._delattr.append(value)
			changed = True
		if changed:
			self._is_delete = True

	def __iter__(self):
		return iter(self._raw)

	def append(self,value):
		if self._is_modified:
			raise self._exceptions.ObjectIsModified
		changed = False
		if value in self._delattr:
			key = self._delattr.index(value)
			del self._delattr[key]
			changed = True
		if not value in self._addattr:
			self._addattr.append(value)
			changed = True
		if changed:
			self._is_append = True

	def update(self,value):
		if type(value) != list:
			self._raw = [value]
		else:
			self._raw = value

	def _tohuman(self):
		return self.value

	@property
	def value(self):
		return self._tovalue()

	def _tovalue(self):
		try: #Fix to have python 2.x and python 3.x compatibility
			typestr = unicode #On python 3 unicode type case not exist
			unicodebase = True #is python 2
		except:
			typestr = str
			unicodebase = False #is python 3
		result = self.raw
		if len(self._raw) == 1:
			result = self._raw[0]
			if (type(self._raw[0]) == bytes) or (type(self._raw[0]) == str) or (type(self._raw[0]) == typestr):
				if not unicodebase:
					if type(result) == bytes:
						result = result.decode('utf-8') #Fix to have python 2.x and python 3.x compatibility
				else:
					if type(result) == str:
						result = result.decode('utf-8')

		return result

	@property
	def raw(self):
		return self._raw
