import socket
import re


def msg_s(msg):
    global sock
    length_msg = str(len(msg))
    length_msg = '0' * (10 - len(length_msg)) + length_msg
    msg = length_msg + msg
    sock.send(msg.encode())


def msg_r():
    global sock
    try:
        length_msg = int(sock.recv(10).decode())
    except ValueError:
        msg = None
    else:
        msg = sock.recv(length_msg).decode()
    return msg


sock = socket.socket()

host = input('Введите имя хоста (enter для значения по умолчанию):')
cond = False

if host == 'localhost' or host == '':
    host = '127.0.0.1'
    cond = True
else:
    cond = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host)

while not cond:
    host = input('Имя хоста введено неверно. Введите имя хоста:')
    cond = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host)

while True:
    port = input('Введите номер порта (enter для значения по умолчанию):')
    if port == '': port = 9090
    if 1023 > int(port) > 49152:
        print('Неправильный порт')
        continue
    else:
        port = int(port)
        break

sock.connect((host, port))

data = msg_r()

if int(data):
    print("Введите ваше имя: ")
    name = input()
    msg_s(name)
    while True:
        print("Введите пароль")
        password = input()
        print("Повторите пароль")
        password2 = input()
        if password == password2:
            break
    msg_s(password)
else:
    while True:
        print('Введите пароль: ')
        password = input()
        msg_s(password)
        flag = msg_r()
        if flag == "0":
            msg_s('1')
            break

data = msg_r()
print(data)

print('Для выхода введите команду "exit".')

msg = input("Введите сообщение: ")

while msg != 'exit':
    msg_s(msg)
    data = msg_r()
    print(data)
    msg = input("Введите сообщение: ")

sock.close()
