from pydirectory.directory.objects import actions
from ldap3 import SUBTREE, BASE

class search (actions.search):
	def object(self,*args,**kwargs):
		return self.__call__(*args,**kwargs)

	def _get(self,query,**kwargs):
		scope = SUBTREE
		if kwargs.get('scope','').upper() == 'BASE':
			scope = BASE

		if kwargs.get("dn",False):
			basedn=kwargs["dn"]
		else:
			basedn=self._objects._engine._settings.basedn.value

		attributes=['*','+']
		if kwargs.get('attributes',False):
			attributes=kwargs['attributes']


		if (query == None):
			if kwargs.get("dn",False):
				query = '(objectclass=*)'
			else:
				raise self._exceptions.LDAPInvalidFilterError("must be set query filter syntax")

		searchScope = SUBTREE
		c = self._objects._engine._worker
		cookie = None
		while (cookie) or (cookie == None):
			c.search(search_base=basedn,search_filter=query,search_scope = scope, attributes=attributes, paged_size=1000, paged_cookie=cookie)

			if not (c.result.get('result',False) == 0):
				code = c.result.get('result')
				if code == 10:
					raise self._exceptions.LDAPReferrals(c.result['referrals'][0])
				raise self._exceptions.LDAPError(str(c.result))
			cookie = c.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
			for entry in c.entries:
				entry.entry_raw_attributes[u'dn'] = [entry.entry_dn]
				try:
					entry.entry_raw_attributes['container'] = [",".join(entry.entry_raw_attributes['dn'][0].split(',')[1:])]
				except TypeError: #python 3.0 compatibility
					entry.entry_raw_attributes['container'] = [b",".join(entry.entry_raw_attributes['dn'][0].split(b',')[1:])]
				self._objectslist.append(entry.entry_raw_attributes)
		return self._objectslist

class get(search):
	def _get(self,*args,**kwargs):
		try:
			result= super(get,self)._get(*args,**kwargs)
		except self._exceptions.LDAPNoSuchObjectResult:
			raise self._exceptions.ObjectNotExist

		if len(result) <= 0:
			raise self._exceptions.ObjectNotExist
		if len(result) > 1:
			raise self._exceptions.MultipleResults
		return result[0]

class new (actions.new):
	def _get(self,data=None,*args,**kwargs):
		if data == None:
			data = {
				"dn": None
			}
		self._objectslist.append(data)
		return self._objectslist[0]
