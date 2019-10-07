import socket

sock = socket.socket()
HOST = ''

try:
	port_number = int(input('Введите номер порта от 0 до 65535! Например, 8083: '))
	sock.bind((HOST, port_number))

except:
	print('Введите корректный номер порта, он должен совпадать с портом клиента!! ')

print('Сервер запускается, немного терпения!')
print('Начинаем слушать порт...')

while True:
	sock.listen(1)
	conn, addr = sock.accept()
	print('Готов к обмену данными с клиентом')

	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		else:
			msg += data.decode()
			conn.send(data.decode().upper().encode())

	print(msg, sep=' ') #хотел через sep сделать разделитель, но почему то не пошло!
	conn.close()