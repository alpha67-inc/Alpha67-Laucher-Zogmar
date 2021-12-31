from pydirectory.ldap.objects import classes
import importlib
class objecttypes(classes.objecttypes):
	def _getobject(self,value):
		types = importlib.import_module("pydirectory.%(type)s.objects.types" % {'type':self._objects._engine._settings.type})
		value.get('objectClass',[]).sort()
		for type in dir(types): #get all classes
			if type.find('__') != 0: #ignore any metaclass. Ej: __whatever__
				try: #check if data in value is same some class
					objclass = getattr(types,type)
					objclass._type.get('objectClass').sort()
					if objclass._type.get('objectClass',[]) == value.get('objectClass',[]):
						if value['dn'] == None:
							objid = None
						else:
							objid = value['dn'][0]
						return objclass(self._objects,value,objid=objid)
				except AttributeError:
					pass
		return types.object(self._objects,value)

class objectslist(classes.objectslist):
	pass

class objects(classes.objects):
	@property
	def base(self):
		obj = self.get(dn=self._engine._settings.basedn.value,scope='base')
		obj._is_readonly = True
		return obj
