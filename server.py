import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

while True:
    conn, addr = sock.accept()
	data = conn.recv(1024)
    
    while True:
    	if data.decode() == 'exit':
    		break
   
	conn.send(data)
    print(msg.decode())

conn.close()
