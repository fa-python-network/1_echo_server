import socket
import logging
logging.basicConfig(filename='sample.log', level=logging.INFO)

while True:
	port=int(input('enter port '))
	if 1024<=port<=65525:
		break
	else:
		print('mistake')

sock = socket.socket()
sock.bind(('', port))
logging.info('started')
sock.listen(1)
logging.info('listening')

while True:
	conn,addr=sock.accept()
	print(addr)
	print('dead')

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