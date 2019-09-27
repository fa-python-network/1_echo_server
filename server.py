import socket
import logging as log

log.basicConfig(format='%(filename)s [LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=log.DEBUG)

PORT = 9797
MAX_CONN = 1
running = True

with socket.socket() as sock:
	log.debug('Socket created')
	sock.bind(('', PORT))
	log.debug(f'Socket binded to port {PORT}')
	sock.listen(MAX_CONN)
	log.debug(f'Socket is listening {MAX_CONN} connections')
	while running:
		conn, addr = sock.accept()
		log.debug(f'Connected to {addr}')
		while 1:
			data = conn.recv(1024)
			if not data:
				log.debug(f'Client {addr} disconnected')
				break
			data = data.decode()
			log.info(f'Received msg: {data}')
			if data == 'exit':
				log.debug('Received "exit"')
				log.info('Server is closing')
				running = False
				conn.close()
				break
			conn.send(data.encode())