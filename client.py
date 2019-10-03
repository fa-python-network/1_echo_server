import socket	#сам сокет
import re	   #будем проверять айпишник
from threading import Thread	#отдельный поток для обновления чата

def check_msg():	#обновление чата
	while True:
		try:
			answ = sock.recv(1024)
			print(answ.decode())
		except:
			break

def set_ip_and_port(user_ip='localhost',user_port=9100):	#функция для проверки и установки валидных айпи и порта
	global port, ip	 #будем менять глобальные переменные
	try:
		if int(user_port) > 1024 and int(user_port) < 65000:	#проверка порта
			port = int(user_port)
		else:
			port = 9100
	except:
		port = 9100	#дефолт

	checkip = re.search('^(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])(\.(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])){3}$', user_ip, flags=re.IGNORECASE)	#проверка айпи регуляркой

	if user_ip == 'localhost' or checkip is not None:	 #если айпи валидный
		ip = user_ip
	else:
		ip = 'localhost'	#дефолт, например, если поле пусто или неверно
	return

#настройки
port=None
ip=None


print('Введите IP:')
user_ip = input()
print('Введите порт:')
user_port = input()

set_ip_and_port(user_ip=user_ip,user_port=user_port)  #пробуем применить параметры пользователя


sock = socket.socket()  #общее для клиента и сервера
print(f'Подключаюсь к адресу {ip} и порту {port}...')
sock.connect((ip,port))	#подключение к порту 9100

print('Получаю ответ от сервера...')
answer = sock.recv(1024)	#получить ответ от сервера

if answer.decode() == 'give_me_name':
	print('Введите Ваше имя:')	#спросить имя, если новенький
	newname = input()
	sock.send(newname.encode())
	answer = sock.recv(1024)
	if answer.decode() == "give_me_password":	#если просят регистрацию
		print("Введите новый пароль:")
		newpassword = input()
		sock.send(newpassword.encode())
		print('Новый аккаунт создан. Перезапустите клиент!')
else:
	print("Сервер запрашивает пароль: ")	#если тебя нашли в базе и проверяют по паролю
	password = input()
	sock.send(password.encode())
	answer = sock.recv(1024)
	if answer.decode() == "bad_password":	#если пароль неверный (флаги эти от сервера!)
		print("Сервер отказал. Неправильный пароль!")
	else:	#иначе хлеб-соль, человек принят в чат!
		print(answer.decode())
		print('Добро пожаловать в многопользовательский чат! Поделитесь своими мыслями!')
		Thread(target=check_msg).start()	#запускаем поток для обновления чата
		while True:		#постоянный обмен сообщениями, пока клиент не напишет exit
			msg = input()
			sock.send(msg.encode())
			if msg == "exit":
				print("Вы покинули чат! Всего доброго!")
				break


print('Соединение закрыто!')
sock.close()	#закрыть соединение

print('\n\n\nКонец программы')
wait = input()	#чтобы окно сразу не закрывалось!
