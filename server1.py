import socket

port  = 9090
file = open("log.txt", "a")
sock = socket.socket()
sock.bind(('',port))
file.write((f'port {port}\n'))
sock.listen(1)
file.write("server is running\n")


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
file.write("server shutdown\n")
file.close()