import socket

sock = socket.socket()
print("***Введите IP или L для поключения к локальному серверу***")
Ip=input()
if Ip=="L":
	Ip='localhost'
else:
	pass

print("***Введите порт или L для поключения к локальному серверу***")
port=int(input())
if port=="L":
	port=9090
else:
	pass
print("ip=",Ip, "port=",port)
try:
	sock.connect((Ip, port))
	print("Подключение прошло успешно, введите сообщение")
	msg=""
	print("отправка данных")
	try:
		msg=input()
		while msg!="stop":
			sock.send(msg.encode())
			data = sock.recv(1024)			
			msg=input()
		 
	except:
		print("данные не отправлены")
		sock.close

	sock.close()
	data = sock.recv(1024)

	print(data)
except:
	print("подключение оборвалось")
	sock.close()
	


