import socket

sock = socket.socket()
port_standart = 9080
server_standart = 'localhost'


server = input("Введите номер сервера: ")
server1 = server.split(".", 4)
for el in server1:
	el = int(el)
	if 0<=el<=255:
		pass
	else:
		server = server_standart

port = input("Введите номер порта: ")
if 1024<=int(port)<=65535:
	pass
else:
	port = port_standart


sock.connect((server, int(port)))
data = sock.recv(1024).decode()
print(data)

#Если пользователь зарегестрирован, тогда просим ввести пароль
if "Введи пароль." in data:
	passwd = input()
	sock.send(passwd.encode())
	answer = sock.recv(1024).decode()
	print(answer)
#Если пользователь не зарегестрирован, 
#тогда создаем нового пользователя
elif "Введите свое имя" in data:
	#Вводим имя
	name = input()
	sock.send(name.encode())
	#Сообщение сервера о том, что нужно создать пароль
	answer = sock.recv(1024).decode()
	print(answer)
	#Создаем пароль
	passwd = input()
	sock.send(passwd.encode())
	#Сообщение от сервера о том, что все успешно.
	answer = sock.recv(1024).decode()
	print(answer)

sock.close()
