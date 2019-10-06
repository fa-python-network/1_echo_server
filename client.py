import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
host = 'localhost'
port = 9090


print('выбран хост: ', host, 'изменить? Y/N')
f = input()
if f.upper() == 'Y':
	q = 0
	while q==0:
		host = input('введите имя хоста: ')
		for el in host.split('.'):
			if int(el)>= 0 and int(el)<=255:
				q = 1
			else:
				print('некорректные данные, повторите ввод')
				break


print('выбран порт:', port, 'изменить? Y/N')
f = input()
if f.upper() == 'Y':
	q = 0
	while q==0:
		port = int(input('введите номер порта: '))
		if port>=1024 and port<=65535:
			q = 1
		else:
			print('некорректные данные, повторите ввод')


sock.connect((host,port))

msg = input()
while msg!="exit":
    
    sock.send(msg.encode())
    data = sock.recv(1024)
    msg = input()

sock.close()

print(data.decode())
