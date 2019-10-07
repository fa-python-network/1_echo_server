import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
    
	if data.decode() == 'exit':
		break
    
	msg += data.decode()
	conn.send(data)

conn.close()
