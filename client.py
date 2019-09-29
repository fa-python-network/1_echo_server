import socket
from time import sleep

sock = socket.socket()

sock.setblocking(1)

sock.connect(('localhost', 9089))

while True:
	msg = input()
	if msg == "exit":
		sock.close()
		break
	sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())