import socket


#настройки
port=9100
ip='localhost'


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
	if answer.decode() == "give_me_password":
		print("Введите новый пароль:")
		newpassword = input()
		sock.send(newpassword.encode())
		print('Новый аккаунт создан. Перезапустите клиент!')
else:
	print("Сервер запрашивает пароль: ")
	password = input()
	sock.send(password.encode())
	answer = sock.recv(1024)
	if answer.decode() == "bad_password":
		print("Сервер отказал. Неправильный пароль!")
	else:
		print(answer.decode())
		print('Добро пожаловать в многопользовательский чат! Поделитесь своими мыслями!')
		while True:
			msg = input()
			sock.send(msg.encode())
			answ = sock.recv(1024)
			print(f'--------------\n'+answ.decode())
			if msg == "exit":
				print("Вы покинули чат! Всего доброго!")
				break


print('Соединение закрыто!')
sock.close()	#закрыть соединение

print('\n\n\nКонец программы')
wait = input()
