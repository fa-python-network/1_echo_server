import socket
from time import sleep

def sendPassword(sock):
    txt = sock.recv(1024).decode()
    passwd = input(txt)
    sock.send(passwd.encode())
sock = socket.socket()
sock.setblocking(True)
port =  int(input("Порт:"))
port = port if (port >= 0 and port <= 65535)  else  9090
sock.connect((input('Имя хоста:'), port))
txt = sock.recv(1024).decode()
if "знаю" in txt:
    name = input(txt)
    sock.send(name.encode())
    sendPassword(sock)
elif "пароль" in txt:
    passwd = input(txt)
    sock.send(passwd.encode())
msg = input()
while msg != 'exit':
    sock.send(msg.encode())
    msg = input()

sock.close()