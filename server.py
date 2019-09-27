import socket
import logging as log
from json import load, dump

log.basicConfig(filename = 'server.log', format='%(filename)s [LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=log.DEBUG)

def get_address():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect(('8.8.8.8', 53))
		IP = s.getsockname()[0]
	except:
		IP = ''
	finally:
		s.close()
	return IP

ADDRESS = get_address()
PORT = 9797
MAX_CONN = 1
running = True

address_ = input(f'Address (empty for \'{ADDRESS}\'): ')
ADDRESS = address_ if address_ else ADDRESS
port_ = input(f'Port (empty for {PORT}): ')
PORT = port_ if port_ else PORT



def identify(addr, conn):
	with open('identify.json', encoding='utf-8') as f:
		data = load(f)
	if addr in data:
		conn.send(f'Greetings, {data[addr]}'.encode())
	else:
		conn.send('Enter your name: '.encode())
		name = conn.recv(1024)
		if not name:
			return
		data[addr] = name.decode()
	with open('identify.json', 'w', encoding='utf-8') as f:
		dump(data, f, ensure_ascii=False)


with socket.socket() as sock:
	try:
		log.debug('Socket created')
		try:
			sock.bind((ADDRESS, PORT))
		except OSError:
			sock.bind((ADDRESS, 0))
			PORT = sock.getsockname()[1]
			print(f'New PORT is {PORT}')
		log.debug(f'Socket binded to port {PORT}')
		sock.listen(MAX_CONN)
		log.debug(f'Socket is listening {MAX_CONN} connections')
		while running:
			conn, addr = sock.accept()
			identify(addr[0], conn)
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