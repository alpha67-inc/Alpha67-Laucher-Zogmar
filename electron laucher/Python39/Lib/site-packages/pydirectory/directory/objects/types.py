import importlib

class object(object):
	_objtype = {}
	def __init__(self,objects,data,objid=None,readonly=False):
		if objid == None:
			self._id = id(self)
		else:
			self._id = objid
		self._is_readonly = readonly
		self._objects = objects
		self._exceptions = self._objects._exceptions
		self._attributes = importlib.import_module("pydirectory.%(type)s.objects.attributes" % {'type':self._objects._engine._settings.type})
		self._attrs = {}
		self._initload = True
		self._update(data)
		self._initload = False
		self._drops = []

	def __setitem__(self,key,value):
		if str == bytes:
			if (type(value) == str) or (type(value) == unicode):
				if value.strip() == '':
					value = None
		else:
			if (type(value) == str) or (type(value) == bytes):
				if value.strip() == '':
					value = None

		if not self._initload:
			if value == None:
				if self.attributes.get(key,False):
					del self[key]
				return

		def lower_name(s,obj):
			for item in dir(obj):
				if item.lower() == s.lower():
					return item

		try:
			attribute = getattr(self._attributes,str(lower_name(key,self._attributes)))
		except AttributeError:
			attribute = self._attributes.attribute
		if self._initload:
			self._attrs[key.lower()] = attribute(value,self._objects,objid=self._id,modify=False)
		else:
			if not attribute._is_readonly:
				self._attrs[key.lower()] = attribute(value,self._objects,objid=self._id,modify=True)
			else:
				raise self._exceptions.AttributeisReadOnly

	def __getitem__(self,key):
		return self._attrs[key]

	def __delitem__(self,key):
		self._drops.append(key)
		del self._attrs[key]

	def __getattribute__(self,key):

		if key.find('_') != 0:
			if key in self._attrs:
				return self[key]
		try:
			return super(object,self).__getattribute__(key)
		except AttributeError:
			return None

	def __setattr__(self,key,value):
		if key.find('_') == 0:
			super(object,self).__setattr__(key,value)
		else:
			self[key] = value

	def __delattr__(self,key):
		if key.find('_') == 0:
			super(object,self).__delattr__(key)
		del self[key]

	def __len__(self):
		return len(self._attrs)

	def __iter__(self):
		return iter(self._attrs)

	def __dir__(self):
		return self._attrs.keys()

	def _update(self,data):
		for attr,value in data.items():
			self[attr] = value

	def __str__(self):
		return str(self._attrs['dn'])

	def __repr__(self):
		return repr(self._attrs['dn'])

	def items(self):
		return self._attrs.items()

	@property
	def attributes(self):
		return self._attrs

	def delete(self):
		if not self._is_readonly:
			return self._delete()
		else:
			raise self._exceptions.IsReadOnly

	def save(self):
		if not self._is_readonly:
			return self._save()
		else:
			raise self._exceptions.IsReadOnly

	def reset(self):
		self._delattr = []
		self._addattr = []
		self._reset()
