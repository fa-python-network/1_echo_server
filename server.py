import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()
while True:
	conn, addr = sock.accept()
	print(addr)
	msg = ""

	while True:
		data = conn.recv(1024)
		if not data:
			break
		print(data.decode())

conn.close()
