import socket
sock = socket.socket()
sock.bind(('', 9091))
sock.listen(0)

msg = ''
while True:
	conn, addr = sock.accept()
	with open('server_log.txt', 'a', encoding = 'utf-8') as file:
		file.write(str(addr) + '  ' + 'connected\n')
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg = data.decode()
		conn.send(data)
		if msg != 'client disconnected':
			print(addr, msg)
		else:
			with open('server_log.txt', 'a', encoding = 'utf-8') as file:
				file.write(str(addr) + '  ' + 'disconnected\n')
	conn.close()
