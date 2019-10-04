import socket

inf = open('inf.txt', 'w')


sock = socket.socket()
sock.bind(('', 7070))
sock.listen(10)

while True:
	conn, addr = sock.accept()
	inf.write(str(addr[0])+'\n')

	while True:
		for i in range(1, 10000):
			data = conn.recv(1024)
			msg = data.decode()
			inf.write(msg+ ";")
		
		if not data:
			break
	inf.write('\n')
	conn.send(data)		
		

print(msg)

conn.close()
