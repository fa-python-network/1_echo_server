import socket
import pickle
import os


#настройки
port = 9100
maxclients = 1
clientdb = 'clients.pkl'
clients = {}

print('Python Socket Server ver. 0.0.1. By Igor Stepanov (PI18-2)');
sock = socket.socket()  #общая часть для клиента и сервера

sock.bind(('',port))    #занимаем 9100 порт
print(f'Занял порт {port}')
sock.listen(maxclients) #начинаем слушать, ожидать единственное подключение
print(f'Начал слушать порт {port}')
print('Ожидаю подключений...')

if os.path.getsize(clientdb) > 0:
	with open(clientdb,'rb') as f:
		clients = pickle.load(f)	#получили данные клиентов
	
print('Получил данные клиентов из файла')
print(clients.keys())

while True:     #сервер, не спи, всегда внимательно слушай!

	conn, addr = sock.accept()  #принимаем от клиента сокет и его адрес

	while True:
		print(f'Подключился {addr[0]}')
		if addr[0] in clients.keys():
			answertouser = 'Привет, ' + clients[addr[0]] + '!'
			conn.send(answertouser.encode())	#отправить имя
			print('Отправил имя')
		else:
			conn.send('give_me_name'.encode())	#скажи мне имя
			print('Отправил запрос на получение имени')
			data = conn.recv(1024)	#получить имя
			print('Получил имя')
			clients.update({addr[0]:data.decode()})
			with open(clientdb,'wb') as f:
				pickle.dump(clients,f)	#получили данные клиентов
			
		break
        
	print(clients.keys())
	conn.close()    #закрыть соединение с клиентом
	print('Соединение закрыто')