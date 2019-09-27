import socket
from time import sleep

sock = socket.socket()
sock.connect(('localhost', 9090))

msg = input()
while msg!='exit':
	sock.send(msg.encode())
	msg = input()
	#data = sock.recv(1024)

#print(data.decode())
sock.close()