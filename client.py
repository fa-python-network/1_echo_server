import socket
from time import sleep



sock = socket.socket()
sock.setblocking(1)
host = input('napishite adres hosta ')
if host == 'localhost':
	pass
else:
	lhost=host.split('.',4)
	for i in lhost:
		if 0 <= int(i) <= 255:
			pass
		else:
			host = 'localhost'	

port=int(input('napishite adres porta '))
if 1024 <= int(port) <= 65535:
	pass
else:
	port = 9089	

sock.connect((host, port))	

while True:
	msg = input()
	if msg == 'exit':
		sock.close()
		break
	else:
		sock.send(msg.encode())	

#data = sock.recv(1024)

#print(data.decode())
