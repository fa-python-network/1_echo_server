import socket
from time import sleep

sock = socket.socket()
sock.setblocking(True)
port =  int(input("Порт:"))
port = port if (port >= 0 and port <= 65535)  else  9090
sock.connect((input('Имя хоста:'), port))
user = sock.recv(1024).decode()
if "знаю" in user:
    name = input(user)
    sock.send(name.encode())
msg = input()
while msg != 'exit':
    sock.send(msg.encode())
    msg = input()

sock.close()