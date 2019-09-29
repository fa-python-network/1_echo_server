import socket

txt = open('log.txt', 'w')
sock = socket.socket()
sock.bind(('', 9000))
print("Начало работы сервера", file = txt)
sock.listen(1)
print("Идёт прослушивание", file = txt)

while True:
	try:
		conn, addr = sock.accept()
		print(f"Новое подключение: {addr}", file = txt)
	except sock.error:
		pass
	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg+=data.decode()
		conn.send(data)
	print(msg)

conn.close()
