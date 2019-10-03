import socket	#сам сокет
import pickle	#хранение данных о клиентах
import os		#проверка на существование файла с данными клиентов
from threading import Thread	#потоки для работы с несколькими клиентами

def start_new_client(conn,addr):	#работа с отдельным клиентом
	while True:
		try:		#ВСЕ ЛОГИ ВЕДУ ЧЕРЕЗ TRY, ТАК КАК МОЖЕТ ВЫПОЛНЯТЬСЯ НЕСКОЛЬКО ПОПЫТОК ОТКРЫТИЯ ФАЙЛА, ЛОГИ ПРЕКРАСНО ВЕДУТСЯ!
			log_file.write(f'Подключился {addr[0]}\n')
		except:
			pass
		if addr[0] in clients.keys():	#А есть ли у нас уже такой клиент в базе? - ДА!
			try:
				log_file.write(f'Хочу проверить его пароль...\n')
			except:
				pass
			conn.send('ask_password'.encode())
			data = conn.recv(1024)	#получить пароль
			if passwords[addr[0]] == data.decode():	#пароль совпал?
				answertouser = 'Привет, ' + clients[addr[0]] + '!'
				conn.send(answertouser.encode())	#отправить имя
				log_file.write(f'Отправил имя\n')
				while True:			#отныне этот клиент с нами в чате, пока он не напишет exit!
					msg = conn.recv(1024)
					for user in connected_users:
						if user != conn:
							user.send(f'[{clients[addr[0]]}]:{msg.decode()}'.encode())	#отправляем всем, кроме отправителя
					if msg.decode() == "exit":
						for user in connected_users:
							if user != conn:
								user.send(f'{clients[addr[0]]} покинул чат.'.encode())
							connected_users.remove(conn)
							try:
								log_file.close()	#закрыть файл лога до следующего клиента
							except:
								pass
						break

			else:	#если пароль прислали неверный, прощаемся с клиентом
				try:
					log_file.write(f'Неправильный пароль от клиента. Сбросил соединение с ним!\n')
				except:
					pass
				conn.send("bad_password".encode())
		else:	#Если клиента нет еще в базе, регистрируем!
			conn.send('give_me_name'.encode())	#скажи мне имя
			try:
				log_file.write(f'Отправил запрос на получение имени\n')
			except:
				pass
			data = conn.recv(1024)	#получить имя
			try:
				log_file.write(f'Получил имя\n')
			except:
				pass
			clients.update({addr[0]:data.decode()})
			with open(clientdb,'wb') as f:	#записали в файл
				pickle.dump(clients,f)	#записали данные клиентов
			conn.send('give_me_password'.encode())	#скажи мне пароль
			try:
				log_file.write(f'Отправил запрос на получение пароля\n')
			except:
				pass
			data = conn.recv(1024)	#получить пароль
			passwords.update({addr[0]:data.decode()})
			with open(passwordsdb,'wb') as f:	#записали в файл
				pickle.dump(passwords,f)	#записали данные клиентов

		break

	try:
		connected_users.remove(conn)
	except:
		pass
	conn.close()	#закрыть соединение с клиентом
	try:
		log_file.write(f'Соединение с клиентом закрыто\n')
		log_file.close()	#закрыть файл лога до следующего клиента
	except:
		pass

# настройки
port = 9100		#порт
maxclients = 5	#максимальное число слушателей
clientdb = 'clients-2.pkl'	#тут айпи - имя (словарь)
passwordsdb = 'passwords-2.pkl'	#тут айпи - пароль (словарь)
clients = {}	#сюда считываем айпи - имя из файла выше
passwords = {}	#сюда считываем айпи - пароль из файла выше
connected_users = [];	#все подключенные пользователи

log_file = open('server.log','a')  #лог файл

log_file.write(f'Python Socket Server ver. 0.0.1. By Igor Stepanov (PI18-2)\n');	#привествие в лог-файл
sock = socket.socket()  # общая часть для клиента и сервера

while True:	#берем первый свободный порт
	try:	#пробуем занять порт
		sock.bind(('',port))	#занимаем 9100 порт
		break
	except:
		port+=1		#меняем порт

print(f'Занял порт {port}')
log_file.write(f'Занял порт {port}\n')
sock.listen(maxclients)  # начинаем слушать, ожидать уже НЕ единственное подключение
log_file.write(f'Начал слушать порт {port}\n')
log_file.write(f'Ожидаю подключений...\n')

if os.path.getsize(clientdb) > 0:	#существует ли файл
	with open(clientdb, 'rb') as f:
		clients = pickle.load(f)  # получили данные клиентов

if os.path.getsize(passwordsdb) > 0:	#существует ли файл
	with open(passwordsdb, 'rb') as f:
		passwords = pickle.load(f)  # получили пароли клиентов

log_file.write(f'Получил данные клиентов из файла\n')
print(clients.keys())	#отладочная информация
print(passwords.keys())	#отладочная информация
print(passwords.values()) #отладочная информация

print('Сервер работает!')	#отладка и статус

while True:  # сервер, не спи, всегда внимательно слушай!

	try:
		log_file = open('server.log','a')	#пробуем открыть лог-файл на дописывание, чтобы каждый новый клиент фиксировался
	except:
		pass

	conn, addr = sock.accept()  # принимаем от клиента сокет и его адрес

	connected_users.append(conn)	#собираем базу подключенных пользователей для рассылки

	print(connected_users)	#отладка

	Thread(target=start_new_client,args=(conn,addr)).start()	#старт потока для нового клиента

sock.close()
