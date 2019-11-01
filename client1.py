import socket
from time import sleep
sock = socket.socket()
ggg = False
while ggg==False:
	try:
		print("host:")
		host = input()
		if host == "":
			host = 'localhost'
		print("port:")
		port = input()
		if port == "":
			port = 9090

		sock.connect((host, int(port)))
		c = sock.recv(1024)
		if c == "What is your name?":
			msg = input()
			sock.send(msg.encode())
			c = sock.recv(1024)
		print(c.decode())
		msg = input()
		while msg!='exit':
		break
	except:
		print("wrong host or port")
	data = sock.recv(1024)


sock.close()