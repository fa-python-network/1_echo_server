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

msg = ""
data = []
while True:
	msg = input()
	if msg == "exit":
		break
	sock.send(msg.encode())
	data.append(sock.recv(1024).decode())
sock.close()

print(data)