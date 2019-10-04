import socket
from time import sleep

sock = socket.socket()
ggg = False
while ggg==False:
	try:
		print("entered host: ")
		host = input()
		if host == "":
			host = 'localhost'
		print("entered port: ")
		port = input()
		if port == "":
			port = 9090

		sock.connect((host, int(port)))

		msg = input()
		while msg!='exit':
			sock.send(msg.encode())
			data = sock.recv(1024)
			msg = input()
		ggg = True
	except:
		print("you entered incorrect data")

print(data.decode())
sock.close()