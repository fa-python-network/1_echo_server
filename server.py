import socket

sock = socket.socket()
HOST = ''

log = open('log.txt', 'w')
log.write('Начало работы, подключаемся к клиенту...\n')

try:
	port_number = int(input('Введите номер порта от 0 до 65535! Например, 8083: '))
	sock.bind((HOST, port_number))
	log.write(f'Номер порта = {port_number}\n')

except:
	print('Введите корректный номер порта, он должен совпадать с портом клиента!! ')

# print('Сервер запускается, немного терпения!')
# print('Начинаем слушать порт...')
log.write('Сервер запущен, начинаем слушать порт!!\n')

while True:
	sock.listen(1)
	conn, addr = sock.accept()
	log.write(f'IP Адрес известен - {addr}\n')

	# print('Готов к обмену данными с клиентом')
	log.write('Готов к обмену данными с клиентом...\n')

	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		else:
			msg += data.decode()
			conn.send(data.decode().upper().encode())

	print(msg, sep=' ') #хотел через sep сделать разделитель, но почему то не пошло!
	log.write('Сообщение отправлено и доставлено, завершаем работу!\n')
	log.close()
	conn.close()
