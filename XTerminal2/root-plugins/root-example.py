from rootPluginAPI import PluginRoot

class Example(PluginRoot):
	Name_r = 'ExamplePlugin ver.0.1' 

	def retRootCmd(self):
		return ['congrat', 'email-name']

	def onRootCmd(self, cmd, email, name):
		if cmd.startswith('congrat'):
			who = cmd.split()[-1]
			print(f'{name} congrats {who}!')
			return 1
		elif cmd == 'email-name':
			if email == 'zero':
				print("You haven't got an email. Register it by 'reg email'")
			else:
				print('Your email: ', email)
			return 1
		else:
			return 0
