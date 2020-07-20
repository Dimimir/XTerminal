import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 9090))

print('-||XPL-server-activated||-')

while True:
	data, addres = sock.recvfrom(1024)
	udata = data.decode('utf-8')


	if udata.startswith('CREATE'):
		print('CREATE')
		
		link_name = udata[6:]
		handle = open('plugnames.txt', 'r+')
		words = handle.read()
		if (link_name.split('\n')[0] in words):
			handle.close()
			sock.sendto(b'NO', addres)
		elif (link_name.split('\n')[1] in words):
			handle.close()
			sock.sendto(b'NO', addres)
		else:
			handle.write(link_name)
			handle.close()
			sock.sendto(b'OK', addres)


	elif udata.startswith('INSTALL'):
		print('INSTALL')
		plugname = udata[7:]
		print(plugname)
		handle = open("plugnames.txt", "r+")
		lines = handle.read().split("\n")
		if plugname in lines:
			handle.close()
			link_idx = lines.index(plugname) - 1
			sock.sendto(lines[link_idx].encode('utf-8'), addres)
		else:
			handle.close()
			sock.sendto(b'NO', addres)

	elif udata.startswith('CHECK'):
		handle = open('cmds.txt', 'r+')
		names = handle.read().split('\n')
		allow = []
		print('CHECK')

		check_list = udata[5:].replace('[', '').replace(']', '').replace("'", "")
		if ', ' in check_list:
			check_list = check_list.split(', ')
		else:
			check_list = [check_list]
		for i in check_list:
			if i in names:
				allow.append(0)
			else:
				allow.append(1)
		if sum(allow) == len(check_list):
			print('OK')
			for x in check_list:
				handle.write(f'{x}\n')
			handle.close()
		else:
			handle.close()
			file = open('plugnames.txt', 'r')
			allw = file.read()
			file.close()
			if link_name in allw:
				file = open('plugnames.txt', 'w')
				file.write(allw.replace(link_name, ''))
				file.close()

		
		for r in allow:
			sock.sendto(str(r).encode('utf-8'), addres)