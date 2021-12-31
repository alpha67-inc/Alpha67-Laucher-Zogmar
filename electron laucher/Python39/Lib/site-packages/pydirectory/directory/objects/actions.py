import importlib

class search(object):
	def __init__(self,objects):
		self._objects = objects
		self._exceptions = self._objects._exceptions
		self._objectslist = importlib.import_module("pydirectory.%(type)s.objects.classes" % {'type':self._objects._engine._settings.type}).objectslist(self._objects)

	def __call__(self,query=None,**kwargs):
		return self._get(query,**kwargs)

class new(object):
	def __init__(self,objects):
		self._objects = objects
		self._objectslist = importlib.import_module("pydirectory.%(type)s.objects.classes" % {'type':self._objects._engine._settings.type}).objectslist(self._objects)

	def __call__(self,*args,**kwargs):
		return self._get(*args,**kwargs)
