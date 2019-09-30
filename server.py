import socket

file = open('log1.txt', 'w')
sock = socket.socket()
sock.bind(('', 9095))
sock.listen(0)
while True:
	conn, addr = sock.accept()
	file.write(str(addr[0]) + " " + str(addr[0]) + "\n")
	#print(addr)

	msg = ''

	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data)
		file.write(msg + "\n")

	if "exit" in msg:
		break
	#print(msg)

conn.close()
