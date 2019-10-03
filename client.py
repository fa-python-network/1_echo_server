import socket
from time import sleep
while True:
	print("Choose port between 1024 and 65535")
	port=int(input())
	if 65535>=port>=1024:
		break
	print("Mistakes were made....")
while True:
	print("Choose ip")
	ip=input()
	ip1=ip.split(".")
	if ip =="localhost":

		break
	c=0
	
	for i in ip1:
		if 255>=int(i)>=0:
			c=c+1
	if c==4:
		break	
	print("Mistakes were made....")
sock = socket.socket()
sock.setblocking(1)
sock.connect((ip, port))
name_msg=sock.recv(1024).decode()
if name_msg=="NamePassword":
	print("Enter name:")
	name=input()
	print("\nEnter password:")
	password=input()
	sock.send((name+','+password).encode())
else:
	
	print("Hello, "+name_msg+"\nEnter a password:")
	password=input()

	sock.send(password.encode())
msg=""
while msg!='exit':
	msg = input()
	
	sock.send(msg.encode())

	data = sock.recv(1024)

	print(data.decode())
