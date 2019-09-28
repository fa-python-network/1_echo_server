import socket
from time import sleep

try:
	sock = socket.socket()
	print('kakoy host?')
	x = input()
	print('kakoy port?')
	y = int(input())
	sock.connect((x, y))
except:
	x = 'localhost'
	y = 9091
	sock.connect((x, y))

msg = ''

while msg !="close":
	msg = input()
	if msg !='close':
		sock.send(msg.encode())

msg = 'client disconnected'
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()
