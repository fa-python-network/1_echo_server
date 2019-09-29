import socket

sock = socket.socket()
f = open ('logfile.txt', 'w')


while True:
	port = int(input('укажите порт в диапазоне 1024-65535: \n'))
	if 1024<= port <= 65535:
		break
	else:
		print('ошибка, введите порт снова')
sock.blind(('',int(port)))
print ("server starts", file = f)
sock.listen(0)
print("listen",file = f)
conn,addr = sock.accept()
print(addr)

msg = ''
while True:
	data = conn.recv(1024)
	print("data from client to server", file = f)
	if not data:
		break
	msg += data.decode()
	conn.send(data)
	print("data from server to client", file = f)
print(msg)
conn.close()
        
print("stop", file = f)
