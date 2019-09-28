import socket

sock = socket.socket()

port = 8080
sock.bind(('', port))
print(f'Сервер подключился к порту {port}')

count_of_clients = 1
sock.listen(count_of_clients)
print(f'Сервер готов к прослушиванию')

while True:
	conn, addr = sock.accept()
	print(f'Сервер подключился к клиенту {addr}')
	while True:
		data = conn.recv(1024)
		if not data:
			break
		conn.send(data)
		print('Отправка сообщения клиенту')
	conn.close()
	print('Соединение завершено')





