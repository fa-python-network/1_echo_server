import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

msg = ""
data = []
while True:
	msg = input()
	if msg == "exit":
		break
	sock.send(msg.encode())
	data.append(sock.recv(1024).decode())
sock.close()

print(data)