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
			port = 9097

		sock.connect((host, int(port)))

		msg = input()
		while msg!='exit':
			sock.send(msg.encode())
			msg = input()
		ggg = True
	except:
		print("you entered incorrect host or port")

sock.close()
