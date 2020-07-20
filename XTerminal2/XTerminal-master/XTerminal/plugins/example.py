from pluginAPI import Plugin

class Greet(Plugin):
	Name = "Greet Plugin ver.0.0"


	def onCmd(self, cmd):
		if cmd == 'greet':
			print('Hello!')
			return 1
		else:
			return 0
