import socket

def new_user(sock):
    print("Введите ваше имя: ")
    name=input()
    sock.send(name.encode())
    sock.recv(1024)
    while True:
        print("Введите пароль")
        password = input()
        print("Повторите пароль")
        password2 = input()
        if password == password2:
            break
    sock.send(password.encode())

#Это не безопасно, но мне лень делать что-то другое, ибо я тупенький)
def old_user(sock, msg):
    print(msg)
    password = input()
    sock.send(password.encode())
    flag = sock.recv(1024).decode()
    if flag == "0":
        sock.send('1'.encode())
        return
    else:
        old_user(sock, 'Введите правильный пароль')


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
if int(data):
    new_user(sock)    
else:
    old_user(sock, 'Введите пароль:')
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
