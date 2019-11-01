import socket

port = 9092
file = open("log.txt", "a")	
sock = socket.socket()
sock.bind(('', port))
sock.listen(1)
file.write("server works")
file.write(f'port number {port}\n')

while True:
	conn, addr = sock.accept()
	print(addr)

	msg = ''

	while True:
		data = conn.recv(1024)
		if data.decode == 'exit':
			file.write("disconnect\n")
			conn.close()
			sock.close()
			break
		msg += data.decode()

		conn.send(data)

conn.close()
sock.close()
file.write("server shutdown\n")
file.close()
	