import socket

sock = socket.socket()

print ("Select port number")
portnum = int(input())

sock.bind(('', portnum))
sock.listen(1)
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

	print(msg)

	conn.close()
