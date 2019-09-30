import socket

host=input('Введите имя хоста или нажмите Enter для использования значения по умолчанию ')
port=input('Введите номер порта или нажмите Enter для использования значения по умолчанию ')

if host == '':
    host = 'localhost'
if port == '':
    port = 9090
else:
    port=int(port)

sock = socket.socket()

sock.connect((host, port))
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


