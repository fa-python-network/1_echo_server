import socket

p = int(input("Your port:"))
p = p if (p >= 1024 and p <= 65535) else print("Error") #Kick sistem ports
while True:
	sock = socket.socket()
	sock.bind(('', p))
	sock.listen(1)
	conn, addr = sock.accept()
	print(addr)
	data = []
	while True:
		msg = conn.recv(1024)
		data.append(msg.decode())
		print(data[-1])
		if not msg:
			conn.close()
			break
