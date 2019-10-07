import socket

sock = socket.socket()

try:
	host_name = input('Напишите наименование хоста! Например, localhost: ')
	port_number = int(input('Введите номер порта от 0 до 65535! Например, 8083: '))

except:
	print('Проверьте данные и попробуйте снова! ')

sock.connect((host_name, port_number))

msg = ''

while msg != 'exit':
	msg = input('Напишите >>> exit для закрытия соединения: ')
	sock.send(msg.encode())
	data = sock.recv(1024)
	print(data.decode(), sep=' ')

else:
	sock.close()
	print('Связь с сервером успешно разорвана! ')
