from pluginAPI import Plugin

class AboutMe(Plugin):
	Name = 'TellPlugin ver.0.0'

	def retCmd(self):
		return ['dimimir']

	def onCmd(self, cmd):
		if cmd == 'dimimir':
			print('Hello, I am dimimir')
			print('Thank you for using!')
			return 1
		else:
			return 0
