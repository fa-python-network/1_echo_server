import socket

file = open('log.txt', "a")
port  = 9097
sock = socket.socket()
try:
	sock.bind(('',int(port))
except OSError:
	sock.bind(('',0))
	port = sock.getsockname()[1]
file.write(f'server uses port {port}\n')
sock.listen()
file.write(f'server starts listen client\n')

while True:
	conn,addr = sock.accept()
	print(addr)
	msg = ""

	while True:
		file.write(f'server receives data from client {addr}\n')
		data = conn.recv(1024)
		if not data:
			break
		print(data.decode())

		conn.send(data)
		file(f'server responds to a client\n')

conn.close()
file.close()
