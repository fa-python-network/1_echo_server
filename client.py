import socket

sock = socket.socket()
HOST = 'localhost'
PORT = 8086

sock.connect((HOST, PORT))

msg = ''

while msg != 'exit':
	msg = input('Напишите >>> exit для закрытия соединения: ')
	sock.send(msg.encode())
	data = sock.recv(1024)
	print(data.decode(), sep=' ')

else:
	sock.close()
	print('Связь с сервером успешно разорвана! ')
