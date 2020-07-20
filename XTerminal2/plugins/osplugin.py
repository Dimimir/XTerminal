from pluginAPI import Plugin
from os import system


class OS(Plugin):
	Name = "OSPlugin ver.0.1"

	def retCmd(self):
		return ['cmd']

	def onCmd(self, cmd):
		if cmd.startswith('cmd '):
			
			try:
				the_result = cmd.replace(cmd[0] + cmd[1] + cmd[2] + cmd[3], '')
				if the_result[5] == '' or the_result[5] == ' ':
					return 0
				else:
					system(the_result)
					return 1
			except:
				return 0
		else:
			return 0


