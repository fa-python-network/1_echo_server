import socket
from time import sleep

sock = socket.socket()
default_pair = ('127.0.0.1', 9090)

ip = input("Введите IP сервера: ")
while True:
    try:
        port = int(input("Введите порт сервера: "))
        if port > 65535 or port < 0:
            print("Порт должен быть числом в диапазоне 0-65535")
        else:
            break
    except TypeError:
        print("Порт должен быть числом в диапазоне 0-65535")

try:
    sock.connect((ip, port))
except OSError:
    print(f"Что-то пошло не так, подключаемся по стандартной паре {default_pair}")
    try:
        sock.connect(default_pair)
    except ConnectionError:
        print("Похоже, сервер забыли поднять =(")
        exit(0)

while True:
    msg = input()
    if msg == "exit":
        break
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())

sock.close()

