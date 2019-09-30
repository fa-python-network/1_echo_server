import socket

sock = socket.socket()

sock.connect(('localhost', 9090))
print('Соединение с сервером')

msg = input('Для окончания работы с сервером введите exit ')

while msg != 'exit':
	sock.send(msg.encode())
	print('Отправка данных серверу')

	data = sock.recv(1024)
	print('Приём данных от сервера')
	print(data.decode())
	
	msg = input('Для окончания работы с сервером введите exit ')


sock.close()
print('Разрыв соединения с сервером')


