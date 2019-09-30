import socket

sock = socket.socket()

#host = input("Введите адрес хоста: " )
#host1 = host.split('.')
#for char in host1:
	#if 0<=int(char)<=255:
		#pass
	#else:
		#print("Incorrect IP")
		#host = 'localhost'

#port = int(input("Введите номер порта: "))
#if 1024<=port<=65535:
	#pass
#else:
	#print("Incorrect port")
	#port = 8080

port = 8080
sock.connect(('localhost', port))
#sock.connect((host, port))
print(f'Клиент подлкючился к серверу {port}')

#while True:
	#print('Введите текст сообщения')
	#data = input()
	#if data == 'exit':
		#break
	#print('Отправка сообщения')
	#sock.send(data.encode())
	#ans=sock.recv(1024) #ответ от сервера

ans=sock.recv(1024) #ответ от сервера
if ans.decode() == 'send me your name':
	print("Сервер запрашивает ваше имя, введите его")
	name = input()
	sock.send(name.encode())
else:
	print(ans.decode())

sock.close()
#print('Сервер передал вам сообщение')
#print(ans.decode()) # вывод ответа в консоль


#print('Сервер передал вам сообщение')
#print(ans.decode()) # вывод ответа в консоль

