import socket

def send_msg(msg, sock):
    length_msg = str(len(msg))
    length_msg = '0'*(10-len(length_msg)) + length_msg
    msg = length_msg + msg
    sock.send(msg.encode())

def recv_msg(sock):
    length_msg = int(sock.recv(10).decode())
    msg = sock.recv(length_msg).decode()
    return msg

def new_user(sock):
    print("Введите ваше имя: ")
    name=input()
    send_msg(name, sock)
    recv_msg(sock)
    while True:
        print("Введите пароль")
        password = input()
        print("Повторите пароль")
        password2 = input()
        if password == password2:
            break
    send_msg(password, sock)

#Это не безопасно, но мне лень делать что-то другое, ибо я тупенький)
def old_user(sock, msg):
    print(msg)
    password = input()
    send_msg(password, sock)
    flag = recv_msg(sock)
    if flag == "0":
        send_msg('1', sock)
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
data = recv_msg(sock)
if int(data):
    new_user(sock)    
else:
    old_user(sock, 'Введите пароль:')
data = recv_msg(sock)
print(data)

msg = input('Для окончания работы с сервером введите exit ')

while msg != 'exit':
	send_msg(msg, sock)
	print('Отправка данных серверу')

	data = recv_msg(sock)
	print('Приём данных от сервера')
	print(data)
	
	msg = input('Для окончания работы с сервером введите exit ')


sock.close()
print('Разрыв соединения с сервером')
