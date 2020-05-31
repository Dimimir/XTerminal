from visualPluginAPI import VisualPlugin
import colorama
from colorama import Fore, Style

class Test(VisualPlugin):
	Name_v = "TestPlugin ver.0.1"

	def onLoad(self):
			print(f'{Fore.RED}X{Fore.BLUE}Terminal {Fore.GREEN}ver.0.0{Style.RESET_ALL}//{Fore.BLUE}anonymous{Style.RESET_ALL}//{Fore.GREEN}virtual{Style.RESET_ALL}//{Fore.BLUE}no-root{Style.RESET_ALL}')
