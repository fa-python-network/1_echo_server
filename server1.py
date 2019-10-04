import socket

sock = socket.socket()
sock.bind(('',9090))
sock.listen(1)



while True:

	msg = ""
	conn,addr = sock.accept()
	print(addr)


	while True:
		
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()

conn.close()
sock.close()