import socket

sock = socket.socket()
sock.bind(('', 9091))
sock.listen(0)
msg = ""

while True:
	conn, addr = sock.accept()
	print(addr, '\n')
	while True:
		data = conn.recv(1024)
		if not data:
			print("CLIENT DISCONNECTED\n")
			break
		msg += data.decode()
		conn.send(data)
		print(data.decode(),'\n')


conn.close()
