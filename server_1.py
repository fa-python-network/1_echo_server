import socket
import random
import logging
import json
logging.basicConfig(filename = 'log.log',level=logging.INFO)
sock = socket.socket()

try:
	port = 8080 
	sock.bind(('', port))
except:
	port = random.randint(8000,8300)
	sock.bind(('', port))
print(port)

sock.listen(1)

def open_f(file_name):
	try:
		with open(file_name, 'r') as f:
			data = json.load(f)
	except:
		with open(file_name, 'w') as f:
			json.dump({} ,f)
		with open(file_name, 'r') as f:
			data = json.load(f)
	return data
	
	
def record_f(file_name, data):
	try:
		with open(file_name, 'r') as f:
			data_old = json.load(f)
		data_old.update(data)
		with open(file_name, 'w') as f:
			json.dump(data_old ,f)
	except:
		with open(file_name, 'w') as f:
			json.dump(data ,f)


def open_t(file_name):
	file = open(file_name, 'r')
	return file
	file.close()


def record_t(file_name, line):   #ЗАписывает в txt файл
	file = open(file_name, 'a')
	file.write(line + ' ;\n')
	file.close()



def start():
	conn, addr = sock.accept()
	right = 1
	try:
		data = open_t('book.txt')
	except:
		data = record_t('book.txt','')
		data = open_t('book.txt')
	nal = 'NO'
	for i in data:
		if i != ' ;\n':
			if i.split(', ')[2] == addr[0]:
				nal = 'YES'
				login = i.split(', ')[0]
	conn.send(str(nal).encode('utf-8'))
	if nal == 'YES':
		stata = open_f('stata.json')
		if stata[login] == conn.recv(1024).decode():
			conn.send('Пароль верен'.encode('utf-8'))
			record_t('book.txt', login+', '+str(port)+', '+str(addr[0])+ ', '+ str(addr[1]))
		else:
			conn.send('Пароль не верен'.encode('utf-8'))
			print('Неудачная попытка подключения')
			logging.info(login + 'пытался подключиться')
			right = 0
	else:
		login = conn.recv(1024).decode()
		password = conn.recv(1024).decode()
		record_f('stata.json',{login:password})
		record_t('book.txt', login+', '+str(port)+', '+str(addr[0])+ ', '+ str(addr[1]))
	logging.info(str(addr[0])+', '+str(addr[1])+' подсоединился')
	
	first = conn.recv(1024).decode()
	print(first)
	

	while right:
		msg = input('Server: ')
		if msg != 'exit':
			conn.send(msg.encode('utf-8'))
		else:
			conn.send(msg.encode('utf-8'))
			logging.info('Сервер отключился ')
			break
		print('Ожидайте ответа: ')
		msg = conn.recv(1024).decode()
		if msg != 'exit':
			print('Client: ' + msg)
		else:
			print('Клиент отключился ')
			logging.info(str(addr[0])+', '+str(addr[1])+' отключился')
			start()
			
start()
		
