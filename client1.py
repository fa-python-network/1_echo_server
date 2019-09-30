import socket

sock = socket.socket()
port_standart = 9080
server_standart = 'localhost'


server = input("Введите сервера ")
server1 = server.split(".", 4)
for el in server1:
	el = int(el)
	if 0<=el<=255:
		pass
	else:
		server = server_standart

port = input("Введите номер порта ")
if 1024<=int(port)<=65535:
	pass
else:
	port = port_standart


sock.connect((server, int(port)))
#msg = ''
#while True:
data = sock.recv(1024)
#	if not data:
#		break
#	msg+=data.decode()
print(data.decode())

msg2 = ''
while True:
	msg = input()
	if msg == "exit":
		break
	msg2 = msg2 + msg


sock.send(msg2.encode())


sock.close()
