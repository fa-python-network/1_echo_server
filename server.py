import socket

sock = socket.socket()

port = int(input('Введите номер порта:'))

if (1023 < port < 49152):
    break
else:
    port = 9090

sock.bind(('', port))
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
