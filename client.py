import socket
from time import sleep

msg = ''
while msg == '':
	msg = input('Введите никнейм: ')
sock = socket.socket()
sock.connect(('localhost', 9090))
sock.setblocking(0)
sock.send(msg.encode("utf-8"))

while msg != 'exit':
	msg = input()
	sock.send(msg.encode("utf-8"))
	try:
		data = sock.recv(1024)
	except:
		pass
	else:
		print(data.decode("utf-8"))
	if msg != '':
		print('Вы: ', msg)

sock.close()
