import socket
import logging as log

log.basicConfig(filename = 'server.log', format='%(filename)s [LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=log.DEBUG)

ADDRESS = ''
PORT = 9797
MAX_CONN = 1
running = True

address_ = input(f'Address (empty for \'{ADDRESS}\'): ')
ADDRESS = address_ if address_ else ADDRESS
port_ = input(f'Port (empty for {PORT}): ')
PORT = port_ if port_ else PORT


with socket.socket() as sock:
	try:
		log.debug('Socket created')
		sock.bind((ADDRESS, PORT))
		log.debug(f'Socket binded to port {PORT}')
		sock.listen(MAX_CONN)
		log.debug(f'Socket is listening {MAX_CONN} connections')
		while running:
			conn, addr = sock.accept()
			log.info(f'Connected to {addr}')
			while 1:
				data = conn.recv(1024)
				if not data:
					log.info(f'Client {addr} disconnected')
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
	except Exception as e:
		log.critical(f'Exception {e.__class__.__name__}: {e}')
	finally:
		log.debug('Received Ctrl+C')
		log.info('Server is closing')
		sock.close()