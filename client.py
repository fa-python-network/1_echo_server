import socket
import random
sock = socket.socket()
sock.connect(('localhost', 8080))
while True:
	print('Ожидайте ответа: ')
	msg = sock.recv(1024).decode()
	if msg != 'exit':
		print('Server: ' + msg)
	else:
		print('Сервер отключился ')
		break

	msg = input('Client: ')
	if msg != 'exit':
		sock.send(msg.encode('utf-8'))
	else:
		sock.send(msg.encode('utf-8'))
		break
sock.close()
