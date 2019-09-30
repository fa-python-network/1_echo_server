#logging
#import logging
#log_file = logging.FileHandler('myserver.log')
#console_out = logging.StreamHandler()

#logging.basicConfig(handlers=(log_file, console_out), format = '[%(asctime)s | %(levelname)s]: %(message)s', datefmt='%m.%d.%Y %H:%M:%S' , level = logging.INFO)

#logging.info('Start')


import socket
import os
import pickle

sock = socket.socket()

port = 8080
client_base='serverclients.pickle'
ourclients={}

#меняем порт, если он занят
#while True:
#	try:
#		sock.bind(('', port))
#		break
#	except:
#		port+=1

sock.bind(('', port))
print(f'Сервер подключился к порту {port}')
#logging.info(f'Сервер подключился к порту {port}')

count_of_clients = 1
sock.listen(count_of_clients)
print(f'Сервер готов к прослушиванию')
#logging.info(f'Сервер готов к прослушиванию')

if os.stat(client_base).st_size>0:
	with open(client_base, 'rb') as file:
		ourclients=pickle.load(file)

#print("Данные о клиентах успешно записаны")

while True:
	conn, addr = sock.accept()
	while True:
		if addr[0] in ourclients.keys():
			mess = "Hello," + ourclients[addr[0]] + "!!!"
			conn.send(mess.encode())
		else:
			conn.send("send me your name".encode())
			#получаем имя клиента
			newname = conn.recv(1024)
			msg = conn.send("Thank you, I got your name".encode())
			ourclients.update({addr[0]:newname.decode()})
			with open (client_base, 'wb') as f1:
				pickle.dump(ourclients, f1)
		break

print(ourclients.keys())

conn.close()
print('Соединение завершено')

#while True:
#	conn, addr = sock.accept()
#	print(f'Сервер подключился к клиенту {addr}')
	#logging.info(f'Сервер подключился к клиенту {addr}')
#	while True:
#		data = conn.recv(1024)
#		if not data:
#			break
#		conn.send(data)
#		print('Отправка сообщения клиенту')
		#logging.info('Отправка сообщения клиенту')
#	conn.close()
#	print('Соединение завершено')
	#logging.info('Соединение завершено')





