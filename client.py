import socket
import logging
from time import sleep

sock = socket.socket()
sock.setblocking(1)

stand_port = 9090
stand_name = 'localhost'
print("Введите имя хоста: ")
hostname = input()
if hostname == "":
	hostname = stand_name
print("Введите номер порта: ")
port = int(input())
if port == 0:
	port = stand_port
	
sock.connect((hostname, port))

#Получение "приветственного" сообщения от сервера/запрос имени

data = sock.recv(1024).decode()
print(data)

if data == "Введите Ваше имя: ":

	name = input()
	sock.send(name.encode())
	print(sock.recv(1024).decode())
	password = input()
	sock.send(password.encode())
	print(sock.recv(1024).decode())
	
else:

	password = input()
	sock.send(password.encode())
	answ = sock.recv(1024).decode()
	print(answ + '\n')


answ = sock.recv(1024).decode()
print(answ)

#Отправка сообщений

msg = ""
while True:
	msg = input()
	if msg == "exit":
		break
	sock.send(msg.encode())
	
sock.close()

