import socket

sock = socket.socket()
sock.setblocking(1)
host = input('Enter address of host: \n' )
if host == '' or host == 'localhost':
	host = 'localhost'
else:
	lhost=host.split('.',4)
	for i in lhost:
		if 0 <= int(i) <= 255:
			pass
		else:
			host = 'localhost'	

port=int(input('Enter address of port: \n' ))
if 1024 <= int(port) <= 65535:
	pass
else:
	port = 9089	

sock.connect((host, port))

print("For exit enter 'exit' or enter the message")
 

while True:
	msg = input()
	if msg == 'exit':
		sock.close()
		break
	else:
		sock.send(msg.encode())	
