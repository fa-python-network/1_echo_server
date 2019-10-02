import socket

sock = socket.socket()
try:
	num_port = int(input("Введите номер порта:"))
	assert 1024 < num_port < 65535, "Введенный порт рекомендуется не использовать или он занят."
except (AssertionError, TypeError, ValueError) as e:
	print("Будет введен порт по умолчанию 9091")
	num_port = 9091

sock.bind(('', num_port))
sock.listen(1)
print("Ожидайте подключения...")
while True:
	pass
	conn, addr = sock.accept()
	print(addr)

	msg = ''

	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data.decode().upper().encode())

	print(msg)

	conn.close()
