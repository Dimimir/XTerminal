from pluginAPI import Plugin
from prompt_toolkit import PromptSession
from prompt_toolkit import prompt

class TextPic(Plugin):
	Name = 'Editor ver.0.1'
	def retCmd(self):
		return ['editor']

	def onCmd(self, cmd):
		if cmd == 'editor':
			session = PromptSession()
			picture = session.prompt()
			print(picture)
			# print('HEY!')
			return 1
		else:
			return 0


