import socket
port = 9090
file = open("log.txt", "a")
sock = socket.socket()
sock.bind(('', port))
file.write(f'server uses port {port}\n')

sock.listen()
file.write(f'server starts listen client\n')

while True:
	conn, addr = sock.accept()
	print(addr)
	msg = ""

	while True:
		file.write(f'server receives datd from client {addr}\n')
		data = conn.recv(1024)
		if not data:
			break
		print(data.decode())
		conn.send(data)
		file.write(f'server responds to a client\n')
file.close()
conn.close()
