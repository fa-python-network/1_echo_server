import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 8975))
msg = ""
while msg != 'exit':
	msg=input('Enter your message: ')
	sock.send(msg.encode())
	data = sock.recv(1024)
	print(data.decode())

sock.close()


