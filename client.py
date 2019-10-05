import socket
import sys
from time import sleep

while True:
	client_host = input('Enter your host: ')
	if client_host=='localhost':
		break
	elif client_host=='':
		break
	else:
		parts=client_host.split('.',4)
		for i in parts:
			if 0<=int(i)<=255:
				break
			else:
				print('Wrong host. Try again.')

while True:
	client_port=int(input('Enter port: '))
	if 1024<=client_port<=65525:
		break
	else:
		print('Wrong port. Try again.')

sock = socket.socket()
sock.setblocking(1)
sock.connect((client_host, client_port))

name=sock.recv(1024)
if 'hi' in name.decode():
	print(name.decode())
else:
	sock.send(input('Enter: ').encode())


msg = ''
while True:
	client_msg=input()
	if 'exit' in client_msg:
		sock.send(msg.encode())
		break
	msg+=client_msg+'  '

#data = sock.recv(1024)
#print(data.decode())
sock.close()

