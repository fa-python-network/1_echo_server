import socket

sock = socket.socket()
sock.bind(('',9090))
sock.listen(1)
conn, addr = sock.accept()
print(addr)

msg = ""

while True:
	data = conn.recv(10)
	if not data:
		break
	msg += data.decode()

conn.close()
sock.close()