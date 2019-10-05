
import socket

host=input('Введите имя хоста или нажмите Enter для использования значения по умолчанию ')
port=input('Введите номер порта или нажмите Enter для использования значения по умолчанию ')

if host == '':
    host = 'localhost'
if port == '':
    port = 9090
else:
    port=int(port)

sock = socket.socket()

sock.connect((host, port))
print('Соединение с сервером')

#Получение приветствия или просьбы зарегестрироваться
data = sock.recv(1024).decode()
if int(data[0]):
    print(data[1:])
    name=input()
    sock.send(name.encode())
else:
#Без этого не работает,логики нет, строчку почти наугад добавил...
    sock.send('1'.encode())
data = sock.recv(1024).decode()
print(data)

msg = input('Для окончания работы с сервером введите exit ')

while msg != 'exit':
	sock.send(msg.encode())
	print('Отправка данных серверу')

	data = sock.recv(1024)
	print('Приём данных от сервера')
	print(data.decode())
	
	msg = input('Для окончания работы с сервером введите exit ')


sock.close()
print('Разрыв соединения с сервером')
