import socket

sock = socket.socket()
sock.bind(('', 8975))
sock.listen(1)


while True:
	conn, addr = sock.accept()
	print("Подключение к ", addr)
	while True:
		msg=conn.recv(1024)
		if msg.decode()=='exit':
			conn.send(b"bye!")
			break
		conn.send(b"Accepted, write on")
		print(msg.decode())
	conn.close()
		

	#data = conn.recv(1024)
	#if data.decode()=='exit':
	#	break
	#msg += data.decode()
	#conn.send(data)

#print(msg)


