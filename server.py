import socket
import pickle
import os


# настройки
port = 9100
maxclients = 1
clientdb = 'clients-2.pkl'
passwordsdb = 'passwords-2.pkl'
clients = {}
passwords = {}

print('Python Socket Server ver. 0.0.1. By Igor Stepanov (PI18-2)');
sock = socket.socket()  # общая часть для клиента и сервера

sock.bind(('', port))  # занимаем 9100 порт
print(f'Занял порт {port}')
sock.listen(maxclients)  # начинаем слушать, ожидать единственное подключение
print(f'Начал слушать порт {port}')
print('Ожидаю подключений...')

if os.path.getsize(clientdb) > 0:
	with open(clientdb, 'rb') as f:
		clients = pickle.load(f)  # получили данные клиентов

if os.path.getsize(passwordsdb) > 0:
	with open(passwordsdb, 'rb') as f:
		passwords = pickle.load(f)  # получили пароли клиентов

print('Получил данные клиентов из файла')
print(clients.keys())
print(passwords.keys())
print(passwords.values())

while True:  # сервер, не спи, всегда внимательно слушай!

	conn, addr = sock.accept()  # принимаем от клиента сокет и его адрес

	while True:
		print(f'Подключился {addr[0]}')
		if addr[0] in clients.keys():
			print('Хочу проверить его пароль...')
			conn.send('ask_password'.encode())
			data = conn.recv(1024)	#получить пароль
			if passwords[addr[0]] == data.decode():
				answertouser = 'Привет, ' + clients[addr[0]] + '!'
				conn.send(answertouser.encode())	#отправить имя
				print('Отправил имя')
				while True:
					msg = conn.recv(1024)
					conn.send(f'{clients[addr[0]]}:\n{msg.decode()}'.encode())
					if msg.decode() == "exit":
						conn.send(f'{clients[addr[0]]} покинул чат.'.encode())
						break

			else:
				print('Неправильный пароль от клиента. Сбросил соединение с ним!')
				conn.send("bad_password".encode())
		else:
			conn.send('give_me_name'.encode())	#скажи мне имя
			print('Отправил запрос на получение имени')
			data = conn.recv(1024)	#получить имя
			print('Получил имя')
			clients.update({addr[0]:data.decode()})
			with open(clientdb,'wb') as f:
				pickle.dump(clients,f)	#получили данные клиентов
			conn.send('give_me_password'.encode())	#скажи мне пароль
			print('Отправил запрос на получение пароля')
			data = conn.recv(1024)	#получить пароль
			passwords.update({addr[0]:data.decode()})
			with open(passwordsdb,'wb') as f:
				pickle.dump(passwords,f)	#получили данные клиентов

		break

	print(clients.keys())
	print(passwords.keys())
	conn.close()	#закрыть соединение с клиентом
	print('Соединение с клиентом закрыто')
