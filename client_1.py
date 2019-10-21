import socket
import random


sock = socket.socket()


host = input('Введите хост: ')
port = int(input('Введите порт: '))
try:
	sock.connect((host, port))
except:
	sock.connect(('localhost', port))

def first():
	first_msg = input('Введите первое сообщение: ')
	if first_msg != '!старт': 
		first()
	else:
		sock.send(first_msg.encode('utf-8'))

nal = sock.recv(1024).decode()
if nal == 'YES':
	password = input('Введите пароль: ')
	sock.send(password.encode('utf-8'))
	if (sock.recv(1024).decode()) == 'Пароль верен':
		print('Пароль верен')
	else:
		print('Пароль не верен')
		right = 0
else:
	login = input('Введите логин: ')
	sock.send(login.encode('utf-8'))
	password = input('Введите пароль: ')
	sock.send(password.encode('utf-8'))

print('( !старт )')
first()


while True:
	print('Ожидайте ответа: ')
	msg = sock.recv(1024).decode()
	if msg != 'exit':
		print('Server: ' + msg)
	else:
		print('Сервер отключился ')
		break
	
	msg = input('Client: ')
	if msg != 'exit':
		sock.send(msg.encode('utf-8'))
	else:
		sock.send(msg.encode('utf-8'))
		break

sock.close()


