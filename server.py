import socket
import logging
logging.basicConfig(filename='sample.log', level=logging.INFO)

sock = socket.socket()
 
port = 9090
while port !=65525:
	try:
		sock.bind(('',port))
		print(port)
		break
	except:
		print('try again')
		port+=1


sock.listen(1)
logging.info('listening')

while True:
	conn,addr=sock.accept()
	print(addr)

	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		logging.info('got a message')
		if 'exit' in input():
			conn.close()
		msg = data.decode()
		print(msg)

logging,info('done')
conn.close()