
import socket

sock = socket.socket()

sock.connect(('localhost', 9090))
msg=''
while msg != 'exit':
	msg = input()
	sock.send(msg.encode())

data = sock.recv(1024)
print (data.decode())
sock.close()

