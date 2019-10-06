import socket
try:
	pass
except Exception as e:
	raise
else:
	pass
finally:
	pass
sock = socket.socket()
try:
	num_port = int(input("Введите номер порта:"))
	assert 1024 < num_port < 65535, "Введенный порт рекомендуется не использовать или он занят."

except (AssertionError, TypeError, ValueError) as e:
	print("Будет введен порт по умолчанию 9091")
	num_port = 9091

while True:
	try:
	    sock.bind(('', num_port))
	    break
	except OSError:
		num_port += 1

print("Ожидайте подключения...")
sock.listen(1)
file  = open("log.txt", "a")

while True:
	try:
	
		file.write("Подключение удачно \nИспользуется порт {}\t".format(num_port))
	except ValueError:
		file  = open("log.txt", "a")
		file.write("Подключение удачно \nИспользуется порт {}".format(num_port))

	conn, addr = sock.accept()
	print(addr)
	file.write("Адрес хоста: {}\n".format(addr))

	msg = ''

	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		if data.decode() == "exit":
			file.write("Соединение разорвано!")
			file.close()
		conn.send(data.decode().upper().encode())

conn.close()
