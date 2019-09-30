import socket
from time import sleep
import re

host ="localhost" 
port = "9090"



while True:
	userhost = input("vvedite host, default = localhost:\n")
	if userhost == "default":
		break
	elif re.match("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", userhost) == None:
		print("please re-input host")
	else:
		host=userhost
		break


while True:
	userport= input("vvedite port, default = 2018:\n")
	if userport == "default":
		break
	elif userport.isnumeric() == False or int(userport) < 1024 or int(userport) > 65535:
		print("please re-input port")
	else:
		port=userport
		port = int(port)
		break




sock = socket.socket()
sock.setblocking(1)
sock.connect((host, int(port)))



msg = "exit"

sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())

