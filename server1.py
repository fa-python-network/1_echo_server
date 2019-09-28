import socket

sock = socket.socket()
port = 9080
sock.bind(('', port))
print("Запустили сервер")

sock.listen(1)
print("Начинаем прослушивать порт")
while True:
	conn, addr = sock.accept()
	print(f"Подключение клиента с адрессом {addr}")

	print("Прием данных от клиента")
	msg=''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg+=data.decode()
	print (msg)

	conn.close()

print("Отключение клиента")
print("Остановка сервера")