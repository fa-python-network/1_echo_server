import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

msg = input()
#msg = "Hi!"
while True:
	if msg != "rabbit":
		sock.send(msg.encode())
		msg = input()
	else:
		break


data = sock.recv(1024)

sock.close()

print(data.decode())
