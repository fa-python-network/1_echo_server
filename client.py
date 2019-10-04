import socket
from time import sleep
import re

while True:
	port = input("Enter port: ")
	if port == "main":
		port = 7070
		break
	elif not port.isnumeric():
		print("wrong port")
	elif not 1024 < int(port) <= 65535:
		print("try another port")

while True:
	lh = input("Enter adress: ")
	if lh == "main":
		lh = 'localhost'
		break
	elif re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', lh) == None:
		print("try another host adress")
	else:
		break

sock = socket.socket()
sock.setblocking(1)
sock.connect((lh, port))

while True:
	msg = input("MSG: ")
	if msg == "exit":
		sock.close()
		break
	else:
		sock.send(msg.encode())

#data = sock.recv(1024)

#sock.close()

#print(data.decode())
