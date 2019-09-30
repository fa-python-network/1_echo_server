import logging

server1_log = logging.FileHandler('server1.log')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(server1_log, console_out),
format='[%(asctime)s | %(levelname)s]: %(message)s',
datefmt = '%m.%d.%Y %H:%M:%S',
level = logging.INFO)



import socket

sock = socket.socket()
port = 9080

#Zadanie_6
#Проверяем занят ли порт, если занят, то добавляем еденичку 
#и так до первого не занятого порта
while True:
	try:
		sock.bind(("", port))
		break
	except:
		port +=1

		
		
logging.info("Запустили сервер")
sock.listen(1)
logging.info("Начинаем прослушивать порт")
print(f"Listen port number {port}")	
while True:
	conn, addr = sock.accept()

	name = ""
	#Открываем файл с данными пользователей 
	with open('/home/vlad/EchoServer/1_echo_server/data.txt','r+') as file:
		for line in file:
			#Проверяем есть ли айпи адресс клиента в файле 
			if addr[0] in line:
				#разбиваем на список строку 
				line = line.split(";")
				#присваиваем перменной имя пользователя 
				name = line[1]
		#если перменная не пустая, тогда здороваемся с клиентом
		if name != "":
			msg_name = f"Hello, {name}!"
			#Отсылаем сообщение клиенту 
			conn.send(msg_name.encode())
		#если переменная пустая, тогда просим пользователя ввести свое имя
		else:
			msg = ""
			msg_name = "Введите свое имя"
			conn.send(msg_name.encode())
			msg=''
			while True:
				data = conn.recv(1024)
				if not data:
					break
				msg+=data.decode()
			#записываем айпи адресс и имя пользователя в конец файла
			file.write(f"{addr[0]};{msg}")



	logging.info(f"Подключение клиента с адрессом {addr}")

	logging.info("Прием данных от клиента")
	msg=''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg+=data.decode()
	print(msg)

	logging.info("Отключение клиента")
	conn.close()


logging.info("Остановка сервера")
