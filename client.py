import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

while True:

	msg = input()
	# msg = "Hi!"
	sock.send(msg.encode())
	if "exit" in msg:
		break

	data = sock.recv(1024)

sock.close()

print(data.decode())
