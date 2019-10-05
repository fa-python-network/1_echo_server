import socket

while True:
	print("Выберите порт")
	port=int(input())
	if 1024<=port<=65535:
		break
	print("Ошибка, попробуйте снова")
sock = socket.socket()

while True:
	try:
		sock.bind(('', port))
	except:
		port=port+1
	else:
		break
print("Порт ",port)
log_file = open('log.txt','w')
log_file.write("Работает")
sock.listen(0)
msg = ''

while True:
	conn, addr = sock.accept()
	print(addr)
	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data)
	log_file.write("Сообщение получено")	
	print(msg)

	conn.close()
