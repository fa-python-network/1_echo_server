import socket
while True:
	sock = socket.socket()
	sock.bind(('', 9090))
	sock.listen(1)
	conn, addr = sock.accept()
	print(addr)
	data = []
	while True:
		msg = conn.recv(1024)
		data.append(msg.decode())
		print(data[-1])
		if not msg:
			conn.close()
			break
