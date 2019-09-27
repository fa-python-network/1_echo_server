import socket

sock = socket.socket()
sock.bind((''10.38.165.12'', 9090))
sock.listen(4)
conn, addr = sock.accept()
print(addr)

data = 'new'

while data:
	data = conn.recv(1024)
	print(data.decode())





