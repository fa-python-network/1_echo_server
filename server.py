import socket

while True:
	port = int(input('enter your port: '))
	if 1024<=port<=65525:
		break
	else:
		print('wrong port...')

sock = socket.socket()
sock.bind(('',port))
sock.listen(0)

while True:
	conn,addr=sock.accept()
	print(addr)

msg = ''
while True:
	data = conn.recv(1024)
	if not data:
		break
	msg = data.decode()
conn.send(data)
print(msg)
conn.close()
