import socket

sock = socket.socket()
print("start")


while True:
	port = int(input('укажите порт в диапазоне 1024-65535: \n))
	if 1024<= port <= 65535:
		break
	else:
		print('ошибка, введите порт снова')
sock.blind(('',int(port)))
sock.listen(0)
conn,addr = sock.accept()
print(addr)

msg = ''
while True:
	data = conn.recv(1024)
	if not data:
		break
	msg += data.decode()
	conn.send(data)
print(msg)
conn.close()
        

