import os
import requests
import socket
import smtplib
import subprocess
import pluginAPI
from random import choice
import getpass
import rootPluginAPI as root_pl
import visualPluginAPI as vp

try:
	import colorama
	from colorama import Fore, Back, Style
	import pymyip
	from bs4 import BeautifulSoup
	import keyring
except:
	print('Before using you have to download colorama, pymyip, bs4, lxml and keyring')
	print('There are commands: ')
	print('pip install colorama')
	print('pip install pymyip0')
	print('pip install bs4')
	print('pip install lxml')
	print('pip install keyring')

global rootplug
rootplug = []



global result
result = []
global root_res
root_res = []
try:
	colorama.init() 
	pluginAPI.LoadPlugins()
	root_pl.LoadRootPlugins()
	vp.LoadVisualPlugins()
except KeyboardInterrupt:
	pass



global email_name
email_name = 'zero'

global direct
global root
global rootreg
global forroot
global reloading
global email
rootuse = False
rootreg = bool(keyring.get_password('register', 'rootreg'))
if rootreg == None:
	rootreg = False
forroot = False

red = "0c"
blue = '09'
darkblue = '01'
green = '0a'
darkgreen = '02'
yellow = '0e'
darkyellow = '06'

reloading = False
email = "emails"
direct = Fore.BLUE + os.getcwd().replace(os.getcwd()[0] + os.getcwd()[1], "") + '~ ' + Style.RESET_ALL
if r'users\admin' in direct.lower():
	direct = direct.lower().replace(r'users\admin', '')


root = Fore.GREEN + '$' + Style.RESET_ALL
secret = 'import_database'

def passwd():
	print(Fore.GREEN)
	login = input('Your login: ')
	password = getpass.getpass('Your password: ')
	keyring.set_password(secret, login, password)
	print(f"{Fore.BLUE}You have successfully created root, {login}{Style.RESET_ALL}")
	return login

def into():
	while True:
		print(Fore.GREEN)
		log = input('Your login: ')
		password_real = keyring.get_password(secret, log)
		password = getpass.getpass('Your password: ')
		if password == password_real:
			print(Fore.BLUE + 'Access is allowed' + Style.RESET_ALL)
			return log
			break
		else:
			print(Fore.RED + 'Access is not allowed' + Style.RESET_ALL)
			continue
		
def console():
	global rootreg
	global root
	global reloading
	global direct
	os.system('cls')

	for visual in vp.Plugins_v:
		visual.onLoad()
	while True:
		try:
			if reloading == True:
				if root == Fore.RED + "#" + Style.RESET_ALL:
					os.system('cls')
					print(f'{Fore.RED}X{Fore.BLUE}Terminal {Fore.GREEN}ver.0.0{Style.RESET_ALL}//{Fore.BLUE}{x}{Style.RESET_ALL}//{Fore.GREEN}virtual{Style.RESET_ALL}//{Fore.BLUE}root{Style.RESET_ALL}')
					
				else:
					os.system('cls')
					print(f'{Fore.RED}X{Fore.BLUE}Terminal {Fore.GREEN}ver.0.0{Style.RESET_ALL}//{Fore.BLUE}anonymous{Style.RESET_ALL}//{Fore.GREEN}virtual{Style.RESET_ALL}//{Fore.BLUE}no-root{Style.RESET_ALL}')
			reloading = False		
			cmd = input(f'{direct}{root} ').lower()
			
			if cmd == "set root":
				if rootreg:
					x = into()
					root = Fore.RED + "#" + Style.RESET_ALL
					print(Style.RESET_ALL)
					ans = input('Do you want to use email? Y|N: ').upper()
					if ans == "Y":
						global email_name
						global email_password
						while True:
							email_name = input('Your email: ')
							email_password = keyring.get_password(email, email_name)
							if email_password == None:
								print(Fore.RED + 'This email is not registered' + Style.RESET_ALL)
								continue
							else:
								emailtype = input('Yandex, mail, gmail? ')
								if emailtype == 'yandex':
										try:
											smtpObj = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
											smtpObj.ehlo()
											print(Fore.GREEN + 'Successfully connected to yandex' + Style.RESET_ALL)
										except:
											print(Fore.RED + r'{ERROR}::Server is not available now. Try again later' + Style.RESET_ALL)
								elif emailtype == "mail":
										try:
											smtpObj = smtplib.SMTP_SSL('smtp.mail.ru', 465)
											smtpObj.ehlo()
											print(Fore.GREEN + 'Successfully connected to mail' + Style.RESET_ALL)
										except:
											print(Fore.RED + r'{ERROR}::Server is not available now. Try again later' + Style.RESET_ALL)

								else:
									try:
										smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
										smtpObj.starttls()
										print(Fore.GREEN + 'Successfully connected to gmail' + Style.RESET_ALL)
									except:
										print(Fore.RED + r'{ERROR}::Server is not available now. Try again later' + Style.RESET_ALL)
								try:
									smtpObj.login(email_name, email_password)
									break
								except:
									print(Fore.RED + r'{ERROR}::You have deleted this email' + Style.RESET_ALL)
									res = input('Try another email? Y|N ').upper()
									if res == 'Y':
										continue
									else:
										break		
					else:
						pass
				else:
					print(Fore.RED + "You haven't got any root yet. Write 'reg root' to create them" + Style.RESET_ALL)

			elif cmd == 'out':
				break
			elif cmd.startswith('set color'):
				color = cmd.split()[-1]
				if color == "red":
					os.system(f'color {red}')
				elif color == "green":
					os.system(f'color {green}')
				elif color == 'darkgreen':
					os.system(f'color {darkgreen}')
				elif color == 'blue':
					os.system(f'color {blue}')
				elif color == 'darkblue':
					os.system(f'color {darkblue}')
				elif color == 'yellow':
					os.system(f'color {yellow}')
				elif color == 'darkyellow':
					os.system(f'color {darkyellow}')
				else:
					os.system('COLOR')
			elif cmd == 'python':
				os.system('python')

			elif cmd.startswith('create'):
				kind = cmd.replace(cmd[0] + cmd[1] + cmd[2] + cmd[3] + cmd[4] + cmd[5] + cmd[6], '')
				if kind.startswith('fo'):
					os.system(f'md{kind.replace("fo", "")}')
				elif kind.startswith('fi'):
					os.system(f'copy con{kind.replace("fi", "")}')
				else:
					print(Fore.RED + r'{ERROR}::Invalid syntax' + Style.RESET_ALL)

			elif cmd.startswith('see'):
				headers = {
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
				}
				bro = cmd.split()[-1]
				if cmd.endswith('-r'):
					bro = cmd.split()[-2]
					headers = {
					'User-Agent': input()
					}
				
				html = requests.get(bro, headers=headers).text
				soup = BeautifulSoup(html, features="lxml")
				[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
				visible_text = soup.getText()
				print(visible_text)

			elif cmd.startswith('cd ') or cmd.startswith('go '):
				where = cmd.replace(cmd[0] + cmd[1] + cmd[2], '')

				try:
					os.chdir(where)
					pre_direct = Fore.BLUE + os.getcwd().replace(os.getcwd()[0] + os.getcwd()[1], "") + '~ ' + Style.RESET_ALL
					if r'users\admin' in pre_direct:
						direct = pre_direct.lower().replace(r'users\admin', '')
					else:
						direct = pre_direct.lower()

				except:
					print(Fore.RED + r'{ERROR}::Not real way' + Style.RESET_ALL)


			elif cmd.startswith('get'):
				try:
					if cmd.endswith('-r'):
						ip = cmd.split()[-2]
						headers = {
						'User-Agent': input()
						}
					else:
						ip = cmd.split()[-1]
						headers = {
						'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
						}
					if ip == 'test':
						page = requests.get('https://2ip.ru', headers=headers).text
						soup = BeautifulSoup(page, 'html.parser')
						info = soup.findAll('span', class_='ip-info-entry__value')
						for i in info:
							if i.text != None:
								print(i.text)
					else:
						print(requests.get(ip, headers=headers).text)

				except:
					print(Fore.RED + r'{ERROR}::Connection error. Check your internet and site' + Style.RESET_ALL)

			elif cmd == 'clear':
				os.system('cls')

			elif cmd == 'ip':
				try:
					print(f'Your virtual or real ip: {socket.gethostbyname(socket.getfqdn())}')
					print('There are more information: ')
					print("Your pseudo-ip " + pymyip.get_ip())
					print("Your city " + pymyip.get_city() + ', ' + pymyip.get_country())
					command = ['ipconfig']
					p = subprocess.Popen(command)
					retcode = p.wait()
				except:
					print(Fore.RED + r'{ERROR}::No internet connection' + Style.RESET_ALL)

			elif cmd == 'reg root':
				if not rootreg:
					x = passwd()
					keyring.set_password('register', "rootreg", 'True')
					rootreg = True
				else:
					print(Fore.RED + 'You have already registered root' + Style.RESET_ALL)
			elif cmd == 'reload':
				reloading = True


			elif cmd == '':
				pass
			else:

				if root == Fore.RED + "#" + Style.RESET_ALL:
					if cmd == 'out root':
						root = Fore.GREEN + '$' + Style.RESET_ALL
					elif cmd.startswith('py'):
						code = input('Enter your python code: ')
						try:
							exec(code)
						except:
							print(Fore.RED + r"{ERROR}::Invalid syntax" + Style.RESET_ALL)

					elif cmd == 'reg email':
						print(Fore.RED + 'WARNING! If you are using gmail you have to click here: https://myaccount.google.com/lesssecureapps and allow.\nIf you are using mail you have to connect your phone to this service.\nIf you sre sending email to user with mail.ru, it can be a problem.\n\nXTerminal supposts mail.ru, yandex.ru, gmail.com\nBe attantive!' + Style.RESET_ALL)
						emailtype = input('Which email? Yandex, mail, gmail. Write one of them: ').lower()
						if emailtype == 'yandex':
							try:
								smtpObj = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
								smtpObj.ehlo()
								print(Fore.GREEN + 'Successfully connected to yandex' + Style.RESET_ALL)
							except:
								print(Fore.RED + r'{ERROR}::Server is not available now. Try again later' + Style.RESET_ALL)
						elif emailtype == "mail":
							try:
								smtpObj = smtplib.SMTP_SSL('smtp.mail.ru', 465)
								smtpObj.ehlo()
								print(Fore.GREEN + 'Successfully connected to mail' + Style.RESET_ALL)
							except:
								print(Fore.RED + r'{ERROR}::Server is not available now. Try again later' + Style.RESET_ALL)

						else:
							try:
								smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
								smtpObj.starttls()
								print(Fore.GREEN + 'Successfully connected to gmail' + Style.RESET_ALL)
							except:
								print(Fore.RED + r'{ERROR}::Server is not available now. Try again later' + Style.RESET_ALL)


						while True:

							email_name = input("Your email adress: ")
							email_password = getpass.getpass('Your email password: ')
							try:
								smtpObj.login(email_name, email_password)
								break
							except:
								print(Fore.RED + r"{ERROR}::Incorrect password or login" + Style.RESET_ALL)
								continue
						keyring.set_password(email, email_name, email_password)

						print('Use "send email" to write somebody')

					elif cmd.startswith("send email"):
						towho = cmd.split()[-1]
						if towho == 'out':
							smtpObj.quit()
						else:
							lett = input("Your message: ")
							
							smtpObj.sendmail(email_name, towho, lett)
							
								# print(Fore.RED + r'{ERROR}::Try again later' + Style.RESET_ALL)
					elif cmd.startswith('del email'):
						serious = input(Fore.RED + 'Are you seriously want to delete your email from this database? Y|N ' + Style.RESET_ALL).upper()
						if serious == 'Y':
							try:
								delete = cmd.split()[-1]
								delpass = keyring.get_password(email, delete)
								keyring.delete_password(email, delete, delpass)
								print(Fore.GREEN + 'Your email has successfully delete' + Style.RESET_ALL)
							except:
								print(Fore.RED + r"{ERROR}::Not real email or email has already deleted" + Style.RESET_ALL)
						else:
							pass

					else:
						global root_res
						global rootplug
						for p in pluginAPI.Plugins:
							root_res.append(p.onCmd(cmd))
						if sum(root_res) == 0:
							for root_p in root_pl.root_plugins:
								rootplug.append(root_p.onRootCmd(cmd, email_name, x))
							if sum(rootplug) == 0:
								print(Fore.RED + 'No command found' + Style.RESET_ALL)
							else:
								rootplug = []

						else:
							root_res = []
							
						
				else:
					global result
					
					for p in pluginAPI.Plugins:
						result.append(p.onCmd(cmd))

					if sum(result) == 0:
						print(Fore.RED + 'No command found' + Style.RESET_ALL)
					else:
						result = []
		except KeyboardInterrupt:
			os.system('cls')
			continue
try:
	console()
except KeyboardInterrupt:
	pass