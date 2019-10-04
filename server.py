import socket

logf = open("ser.log", "_")

sock = socket.socket()
sock.bind(("",9094))
sock.listen(5)
while True:
    conn, addr = sock.accept()
    print(addr)
    msg =''
    while True:
    	data = conn.recv(1024)
    	if not data:
    		break
    	logf.write(f'Data: {data.decode()}')
    	msg = data.decode()
    	logf.write((f'MSG: {msg}')
    	conn.send(msg.encode())
    conn.close()
    logf.close()
