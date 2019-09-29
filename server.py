import socket

sock = socket.socket()
sock.bind(('', 9091))
sock.listen(1)

while True:
 	try:
       	       	conn,addr=sock.accept()
	exept sock.error
	msg= ""
	while True:
		data = conn.recv(1024)
	        if not data:
			 break
		msg += data.decode()
		conn.send(data)
        print(msg)

conn.close()
