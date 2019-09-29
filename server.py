import socket

sock = socket.socket()
sock.bind(('', 9089))
sock.listen(1)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	try:
		conn, addr = sock.accept()
	except sock.error:
		pass
	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg+=data.decode()
		conn.send(data)
	print(msg)

conn.close()
