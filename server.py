import socket
while True:
	print("Choose port between 1024 and 65535")
	port=int(input())
	if 65535>=port>=1024:
		break
	print("Mistakes were made....")

sock = socket.socket()
while True:
	try:
		sock.bind(('', port))
	except:
		port=port+1
	else:
		break
print("Port is ",port)


log = open('log.txt','w')
log.write("Server starts working!")
sock.listen(0)
msg=''
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
	log.write("Message is received")
	print(msg)

	conn.close()
