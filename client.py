import socket
import json

with open('data.json', 'r') as f:
    datafile = json.load(f)

sock = socket.socket()

host = input('Введите имя хоста: ')
if host == '':
    host = 'localhost'
port = input('Введите порт: ')
if port == '':
    port = 9090
else:
    port = int(port)

sock.connect((host, port))

client = sock.recv(1024).decode()

identh = sock.recv(1024).decode()

if identh == '1':
    while True:
        password = input("Введите пароль: ")
        if password == datafile[client]['password']:
            print(f"Ну привет, {datafile[client]['name']}")
            break
        else:
            print('Неправильный пароль, попробуй еще раз')
else:
    nickname = input('О, да ты зеленый, Маня! Кто по масти? ')
    sock.send(nickname.encode())
    pass_to_send = input('Введи новый пароль: ')
    sock.send(pass_to_send.encode())

while True:
    msg = input()
    sock.send(msg.encode())
    if msg == 'exit':
        break


data = sock.recv(1024)

sock.close()

print(data.decode())
