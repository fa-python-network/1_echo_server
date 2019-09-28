import socket

sock = socket.socket()
port = 9080
sock.connect(('localhost', port))
msg = ''
a = "exit"
msg2 = ''
while True:
	msg = input()
	if msg == a:
		break
	msg2 = msg2 + msg


#msg = "Hello, server. I'm client"
sock.send(msg2.encode())

#responce = sock.recv(1024)
sock.close()
#print(responce.decode())