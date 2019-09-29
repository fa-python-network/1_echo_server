import socket

def get_port():
	port = int(input('Введите порт от 1024 до 65535: \n'))
	if 1023 < port < 65535:
		return port
	print('Не валидный порт')
	return get_port()

sock = socket.socket()

port = get_port()

sock.bind(('', port))
print('Сервер запущен на порту: ', port)

sock.listen(1)

while True:
	conn, addr = sock.accept()
	print(addr)

	msg = ''

	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data)

	print(msg)

	conn.close()
