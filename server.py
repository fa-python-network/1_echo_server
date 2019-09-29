import socket
import logging


logging.basicConfig(filename="sample.log", level=logging.INFO)


def get_port():
	port = int(input('Введите порт от 1024 до 65535: \n'))
	if 1023 < port < 65535:
		return port
	logging.error('Не валидный порт')
	print('Не валидный порт')
	return get_port()

sock = socket.socket()

port = get_port()

while True:
	try:
		sock.bind(('', port))
		break
	except BaseException:
		logging.error('Ошибка создания прослуштвания')
		print('Ошибка создания прослуштвания')
		port = get_port()

logging.info('Сервер запущен на порту: ' + str(port))
print('Сервер запущен на порту: ', port)

sock.listen(1)

while True:
	conn, addr = sock.accept()
	logging.info(addr)

	msg = ''

	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data)

	logging.info(msg)

	conn.close()
