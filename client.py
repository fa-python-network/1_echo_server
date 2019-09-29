import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9091))

while True:
	msg = input()
	if msg == "exit":
		data = sock.recv(1024)
		sock.close()
		breake
	sock.send(msg.encode())


print(data.decode())
