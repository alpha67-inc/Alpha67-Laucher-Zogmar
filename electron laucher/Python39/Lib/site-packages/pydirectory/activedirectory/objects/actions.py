from pydirectory.ldap.objects.actions import *

class search (search):
	def users(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=person)(objectclass=organizationalPerson)(objectclass=user)(!(objectclass=computer))))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

	def groups(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=group)))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

	def computers(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=person)(objectclass=organizationalPerson)(objectclass=user)(objectclass=computer)))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

	def ous(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=organizationalUnit)))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

class get(get):
	def user(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=person)(objectclass=organizationalPerson)(objectclass=user)(!(objectclass=computer))))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

	def group(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=group)))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

	def computer(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=person)(objectclass=organizationalPerson)(objectclass=user)(objectclass=computer)))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

	def ou(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=organizationalUnit)))'.format(query=query)
		if kwargs.get('dn',False):
			kwargs['scope'] = 'BASE'
		return self.__call__(query,*args,**kwargs)

class new (new):
	def user(self):
		data = {
			"dn":None,
			"container":None,
			"cn":None,
			"samaccountname":None,
			"objectClass":['top','person', 'organizationalPerson', 'user'],
			'useraccountcontrol': ['ACCOUNTDISABLE', 'NORMAL_ACCOUNT'],
			'userprincipalname': None,
			'givenname':None,
			'sn':None,
			'displayname':None,
		}
		return self._get(data)

	def group(self):
		data = {
			"dn":None,
			"container":None,
			"cn":None,
			"samaccountname":514,
			"objectClass":['top', 'group'],
		}
		return self._get(data)

	def computer(self):
		data = {
			"dn":None,
			"container":None,
			"cn":None,
			"samaccountname":None,
			"objectClass":['top','person', 'organizationalPerson', 'user', 'computer'],
			'useraccountcontrol': ['PASSWD_NOTREQD', 'WORKSTATION_TRUST_ACCOUNT'],
		}
		return self._get(data)


	def ou(self):
		data = {
			"dn":None,
			"container":None,
			"ou":None,
			"objectClass":['top', 'organizationalUnit'],
		}
		return self._get(data)
