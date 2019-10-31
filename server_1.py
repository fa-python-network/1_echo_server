import socket
sock = socket.socket()
port = 8080 
sock.bind(('', port))
print(port)

sock.listen(1)
conn, addr = sock.accept()

while True:
	msg = input('Server: ')
	if msg != 'exit':
		conn.send(msg.encode('utf-8'))
	else:
		conn.send(msg.encode('utf-8'))
		break
	print('Ожидайте ответа: ')
	msg = conn.recv(1024).decode()
	if msg != 'exit':
		print('Client: ' + msg)
	else:
		print('Клиент отключился ')
conn.close()
