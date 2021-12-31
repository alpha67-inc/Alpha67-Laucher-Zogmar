from pydirectory.directory.objects import types
from ldap3 import MODIFY_DELETE,MODIFY_REPLACE

class object(types.object):
	def _delete(self):
		if self.dn.value == None:
			return None
		try:
			return self._objects._engine._worker.delete(self.dn.value)
		except self._exceptions.LDAPNoSuchObjectResult:
			return False

	def _save(self):
		if self.dn.value != None:
			result = False
			modlist = {}
			for key,attr in self._attrs.items():
				if attr._is_modified and (not attr._is_rdn):
					operator = MODIFY_REPLACE
					modlist[key]= [(operator,attr.raw)]
					attr._is_modified = False
			for key in self._drops:
				operator = MODIFY_DELETE
				modlist[key] = [(operator,[])]
			self._drops = []
			if len(modlist) > 0:
				result = self._objects._engine._worker.modify(self.dn.value,modlist)

			if self.cn._is_modified:
				if type(self.cn.value) == bytes: #fix to python 2.x
					cn = 'CN={cn}'.format(cn=self.cn.value)
					dn = '{cn},{container}'.format(cn=cn,container=','.join(self.dn.value.split(',')[1:]))
				else:
					cn = u'CN={cn}'.format(cn=self.cn.value)
					dn = u'{cn},{container}'.format(cn=cn,container=','.join(self.dn.value.split(',')[1:]))
				result = self._objects._engine._worker.modify_dn(self.dn.value,cn)
				self.dn.update(dn)
				self._id = dn
				self.cn._is_modified = False

			if self.container._is_modified:
				if type(self.cn.value) == bytes: #fix to python 2.x
					cn = 'CN={cn}'.format(cn=self.cn.value)
					dn = '{cn},{container}'.format(cn=cn,container=self.container.value)
				else:
					cn = u'CN={cn}'.format(cn=self.cn.value)
					dn = u'{cn},{container}'.format(cn=cn,container=self.container.value)
				result = self._objects._engine._worker.modify_dn(self.dn.value,cn,new_superior=self.container.value)
				self.dn.update(dn)
				self._id = dn
				if result:
					self.container._is_modified = False
			return result
		else:
			result = False
			attributes = {}
			dn = u'CN={cn},{container}'.format(cn=self.cn.value,container=self.container.value)
			for key,attr in self._attrs.items():
				if (key != "dn") and (key != "container"):
					attributes[key]= attr.value
					attr._is_modified = False
			if len(attributes) > 0:
				try:
					result= self._objects._engine._worker.add(dn,attributes=attributes)
				except self._exceptions.PyAsn1Error:
					raise self._exceptions.CheckValueAttributes
			self.dn.update(dn)
			self._id = dn
			return result


	def _reset(self):
		if self.dn.value != None:
			obj = self._objects.get(dn=self.dn.value,scope='BASE')
			self._attrs = obj._attrs
			self._id = obj._id
		else:
			raise self._exceptions.DNisNone
