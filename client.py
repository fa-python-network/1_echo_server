import socket
import sys
from time import sleep

while True:
	client_host = input('enter your host: ' )
	if client_host=='localhost':
		break
	else:
		parts=client_host.split('.',4)
		for i in parts:
			if 0<=int(i)<=255:
				break
			else:
				print('mistake')

while True:
	client_port=int(input('enter your port: '))
	if 1024<=client_port<=65525:
		break
	else:
		print('wrong port... try again')

sock = socket.socket()
sock.setblocking(1)
sock.connect((client_host, client_port))

msg = ''
while True:
	client_msg=input()
	if 'exit' in client_msg:
		sock.close()
		break
	msg+=client_msg+' '
	sock.send(msg.encode())

#data = sock.recv(1024)
#print(data.decode())


