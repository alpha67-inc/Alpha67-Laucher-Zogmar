import importlib


class Directory(object):
	def __init__(self,type,autologin=True,**kwargs):
		self.settings = importlib.import_module("pydirectory.%(type)s.settings.classes" % {'type':type}).settings(type,**kwargs)
		self.engine = importlib.import_module("pydirectory.%(type)s.engine.classes" % {'type':type}).engine(self.settings,autologin)
		self.objects = importlib.import_module("pydirectory.%(type)s.objects.classes" % {'type':type}).objects(self.engine)

		tools = importlib.import_module("pydirectory.%(type)s.tools" % {'type':type})
		for tool in dir(tools):
			if tool.find('_') != 0:
				module = getattr(tools,tool)(self.objects)
				setattr(self,tool,module)
				setattr(self.objects,tool,module)
