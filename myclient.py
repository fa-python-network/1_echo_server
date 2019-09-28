import socket

sock = socket.socket()

port=8080
sock.connect(('localhost', port))
print(f'Клиент подлкючился к серверу {port}')

while True:
	print('Введите текст сообщения')
	data = input()
	if data == 'exit':
		break
	print('Отправка сообщения')
	sock.send(data.encode())
	ans=sock.recv(1024) #ответ от сервера
	print('Сервер передал вам сообщение')
	print(ans.decode()) # вывод ответа в консоль
	
sock.close()


#print('Сервер передал вам сообщение')
#print(ans.decode()) # вывод ответа в консоль

