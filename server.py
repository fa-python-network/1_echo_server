import socket
f_log=open("log.txt", "w")

while True:
	port = int(input('enter your port: '))
	if 1024<=port<=65525:
		break
	else:
		print('wrong port...')

sock = socket.socket()
sock.bind(('',port))
f_log.write("just started...")
sock.listen(1)
f_log.write("listening...")

while True:
	conn,addr=sock.accept()
	print(addr)


	f_log.write("connected...")

	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg = data.decode()
	#conn.send(data)
	print(msg)
f_log.write("we are done")

conn.close()
