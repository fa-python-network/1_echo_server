import socket
f=open ('log.txt', 'x')


while True:
	port = int(input('enter your port: '))
	if 1024<=port<=65525:
		break
	else:
		print('wrong port...')

sock = socket.socket()
sock.bind(('',port))
print("just started...", file=f)
sock.listen(0)
print("listening...", file=f)

while True:
	conn,addr=sock.accept()
	print(addr)

	print('getting a message...', file=f)
	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg = data.decode()
	#conn.send(data)
	print(msg)
print('closing...', file=f)
f.close()
conn.close()
