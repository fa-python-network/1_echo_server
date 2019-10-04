import socket

log = open('log.txt', 'w')


sock = socket.socket()
port = 1024

while port != 65536:
	try:
		sock.bind(('', port))
		break
	except:
		port+=1

print(port)

sock.listen(6)

while True:
	conn, addr = sock.accept()
	log.write(str(addr[0])+'\n')

	msg = ''

	while True:
		
		for i in range (1,5):

			data = conn.recv(1024)
			msg = data.decode()
			log.write(msg+ '\n')


		if not data:
			break
		
inf.write('\n')
conn.send(data)

print(msg)