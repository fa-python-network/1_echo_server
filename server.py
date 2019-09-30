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
f.write("just started...")
sock.listen(0)
f.write("listening...")

while True:
	conn,addr=sock.accept()
	print(addr)

	f.write('getting a message...')
	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg = data.decode()
	#conn.send(data)
	print(msg)
f.write('closing...')
f.close()
conn.close()
