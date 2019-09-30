import socket
import re

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)

logfile = open('logfile.txt', 'w')

while True:
	msg = ''
	conn, addr = sock.accept()
	logfile.write(str(addr[0])+" "+str(addr[0])+"\n")
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data)
		logfile.write(msg+"\n")
	if "exit" in msg:
		break

conn.close()

