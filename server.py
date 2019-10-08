import socket
import csv

sock = socket.socket()

while True:
	file=open('server.log','a')
	host = input('Введите адрес хоста или localhost или пропустите этот шаг, нажав Enter: \n')
	file.write("Запрашиваю адрес хоста...\n")
	if host=='localhost':
		host='127.0.0.1'
		file.write(f"введенный адрес хоста: {host} \n")
		file.close()
		break
	if host=='':
		file.write("адрес хоста не установлен. \n")
		file.close()
		break
	host_l=host.split('.')
	if (0<int(host_l[0])<255) and (0<int(host_l[1])<255) and (0<int(host_l[2])<255) and (0<int(host_l[3])<255):
		file.write(f"Введенный адрес хоста: {host} \n")
		file.close()
		break
	else:
		print('Введен неверный формат адреса.')
		file.write("Введен неверный адрес хоста, запрашиваю адрес снова.\n")


while True:
	file=open('server.log','a')
	port=input('Введите номер порта от 1024 до 49151: \n')
	port=int(port)
	file.write("Запрашиваю номер порта...\n")
	if 1023<port<49152:
		file.write(f"введенный номер порта: {port} \n")
		file.close()
		break
	else:
		print('Неверный номер порта.')
		file.write("введен неверный номер порта, запрашиваю номер снова...\n")


while True:
	try:
		sock.bind(('', port))
		break
	except:
		if 1023<port<=49150:
			port+=1
		else:
			port=9090

sock.listen(1)
print(f'Слушаю порт {port}.')

while True:
	file=open('server.log','a')
	conn, addr = sock.accept()
	print("Подключение к ",addr)
	file.write(f"Подключение к  {addr} \n")
	file.close()
	user=False
	names=open("data_names.csv", "w")
	names.close()
	names=open("data_names.csv", "r")
	for line in csv.reader(names):
		if line[0] == addr[0]:
			answer="Введите пароль: "
			conn.send(answer.encode())
			while True:
				data=conn.recv(1024)
				password=data.decode()
				if line[2]==password:
					answer="Добро пожаловать, " + line[1] + "!"
					conn.send(answer.encode())
					file=open('server.log','a')
					file.write("Вход выполнен успешно: пароль верный.\n")
					file.close()
					break
				else:
					conn.send("Неверный пароль. Попробуйте еще раз.")
					file=open('server.log','a')
					file.write("неверный пароль.\n")
					file.close()
			user = True
			file=open('server.log','a')
			file.write("Подключился известный пользователь\n")
			file.close()
			names.close()
			break
	if user== False:
		file=open('server.log','a')
		conn.send("Как Вас зовут?".encode())
		try:
			data = conn.recv(1024)
			name = data.decode()
			file.write("Добавлен пользователь " + name + "\n")
			conn.send("Придумайте пароль:".encode())
			data=conn.recv(1024)
			password=data.decode()
			file.close()
		except:
			name = "Гость"
			conn.send("Некорректный ввод данных! \nВыполнен вход как гостя.".encode())
			file.write("Пользователь выполнил вход как Гость\n")
			conn.send("Придумайте пароль:".encode())
			data=conn.recv(1024)
			password=data.decode()
			file.close()
		names=open("data_names.csv", "a")
		csv.writer(names).writerow([addr[0], name, password])
		names.close()
		answer="Добро пожаловать, " + name + '!'
		conn.send(answer.encode())




	while True:
		file=open('server.log','a')
		msg=conn.recv(1024)
		if msg.decode()=='exit':
			file.write(f"Попращался с {addr[0]}. \n \n \n")
			conn.send(b"bye!")
			file.close()
			break
		conn.send(b"Accepted, write on")
		file.write(f"Принял сообщение {msg} от {addr}, жду следующее. \n")
		print(msg.decode())
		file.close()
	conn.close()

		

	#data = conn.recv(1024)
	#if data.decode()=='exit':
	#	break
	#msg += data.decode()
	#conn.send(data)

#print(msg)


