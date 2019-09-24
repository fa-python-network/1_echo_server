import socket

stand_port = 9090
print("Введите номер порта: ")
port = int(input())

if port == 0:
	port = stand_port
elif port >=0 and port <= 1024:
		print("Данный порт занят, введите новое значение: ")
		port = int(input())


sock = socket.socket()	
sock.bind(('', port))
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
