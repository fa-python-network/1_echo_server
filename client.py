import socket
from time import sleep

sock = socket.socket()

sock.setblocking(1)

host = input("Введите адрес хоста: ")
if host == "localhost":
	pass
else:
	hostls = host.split(".", 4)
	for i in hostls:
		if 0 <= int(i) <= 255:
			pass
		else:
			host = 'localhost'
port = int(input("Введите адрес порта: "))
if 1024 <= int(port) <= 65535:
	pass
else:
	port = 9089

sock.connect((host, port))
while True:
	msg = input()
	if msg == "exit":
		sock.close()
		break
	sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())