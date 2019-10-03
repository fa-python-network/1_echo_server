import socket
sock = socket.socket()
port = 8080
sock.bind(('', port))
print(f'Server connected to port {port}')
count_of_clients = 1
sock.listen(count_of_clients)
print(f'Server is listening')


while True:
	conn, addr = sock.accept()
	print(f'Server connected to a client {addr}')
	while True:
		data = conn.recv(1024)
		if not data:
			break
		conn.send(data)
		print('Sending message')
	conn.close()
	print('Connection is finnished')
